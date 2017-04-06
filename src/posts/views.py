from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .utils import get_posts_from_page, render_post_list
from tagging.views import TaggedObjectList
from django.views.generic import ListView, DetailView

from .models import Post


def index(request):
    page = request.GET.get('page')

    return render_post_list(request, get_posts_from_page(page))


class PostsList(ListView):
    template_name = 'posts/list.html'
    context_object_name = 'posts'
    paginate_by = 5
    model = Post
    queryset = Post.published_objects.all()

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


class PostDetailView(DetailView):
    queryset = Post.published_objects.all()
    model = Post
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


def list(request):
    page = request.GET.get('page')

    # If a page parameter is not present in url
    # let the index view handle the request
    # so that "/posts/" route redirects to  "/"
    if not page:
        return redirect('posts:index', permanent=True)

    return render_post_list(request, get_posts_from_page(page))


def detail(request, slug):
    post = get_object_or_404(Post.published_objects, slug=slug)

    try:
        previous = post.get_previous_by_created_at()
    except Post.DoesNotExist:
        previous = None

    try:
        next = post.get_next_by_created_at()
    except Post.DoesNotExist:
        next = None

    return render(request, 'posts/detail.html', {
        'post': post,
        'previous': previous,
        'next': next
    })


class TaggedPostsList(TaggedObjectList):
    model = Post
    paginate_by = 5
    allow_empty = True
    template_name = 'posts/list.html'
    context_object_name = 'posts'
