from .factories import PostFactory
from .models import Post


def create_posts(unpublished, published):
    for i in range(unpublished + published):
        is_published = i >= unpublished
        PostFactory.create(is_published=is_published)
