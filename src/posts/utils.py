from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

from .models import Post


def get_posts_from_page(page_number):
    published_posts = Post.published_objects.all()
    paginator = Paginator(published_posts, 5)  # Show 5 posts per page

    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    return posts


def render_post_list(request, posts):
    return render(request, 'posts/list.html', {
        'posts': posts
    })
