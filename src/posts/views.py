from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Post


def index(request):
    published_posts = Post.published_objects.all()
    paginator = Paginator(published_posts, 5)  # Show 5 posts per page

    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    return render(request, 'posts/index.html', {
        'posts': posts
    })


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
