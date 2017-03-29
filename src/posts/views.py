from django.shortcuts import render, get_object_or_404

from .models import Post


def index(request):
    posts = Post.published_objects.all()

    return render(request, 'posts/index.html', {
        'posts': posts
    })


def detail(request, slug):
    post = get_object_or_404(Post.published_objects, slug=slug)

    return render(request, 'posts/detail.html', {
        'post': post
    })
