from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .utils import get_posts_from_page, render_post_list

from .models import Post


def index(request):
    page = request.GET.get('page')

    return render_post_list(request, get_posts_from_page(page))


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

    print(request.get_raw_uri())

    return render(request, 'posts/detail.html', {
        'post': post,
        'previous': previous,
        'next': next
    })
