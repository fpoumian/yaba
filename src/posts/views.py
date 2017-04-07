from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .utils import get_posts_from_page, render_post_list
from tagging.views import TaggedObjectList
from django.views.generic import ListView, DetailView

from .models import Post


class BasePostsMixin():
    model = Post
    queryset = Post.published_objects.all()


class BasePostsListMixin():
    template_name = 'posts/list.html'
    context_object_name = 'posts'
    paginate_by = 5


class PostsList(BasePostsMixin, BasePostsListMixin, ListView):
    def get(self, request, *args, **kwargs):
        page = request.GET.get('page')

        # If a page parameter is not present in url
        # let the index view handle the request
        # so that "/posts/" route redirects to  "/"
        if not page:
            return redirect('posts:index', permanent=True)
        return super().get(self, request, *args, **kwargs)


class IndexView(PostsList):
    def get(self, request, *args, **kwargs):
        # return the get() method from grandparent class (ListView)
        # to avoid infinite redirects
        return ListView.get(self, request, *args, **kwargs)


class PostDetailView(BasePostsMixin, DetailView):
    template_name = 'posts/detail.html'

    def get_context_data(self, **kwargs):
        post = self.object
        context = super(PostDetailView, self).get_context_data(**kwargs)

        try:
            context['previous'] = post.get_previous_by_created_at()
        except Post.DoesNotExist:
            context['previous'] = None

        try:
            context['next'] = post.get_next_by_created_at()
        except Post.DoesNotExist:
            context['next'] = None

        print(context)

        return context


class TaggedPostsList(BasePostsMixin, BasePostsListMixin, TaggedObjectList):
    allow_empty = True
