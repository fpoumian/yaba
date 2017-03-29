from django.db import models
from django.urls import reverse
from markdownx.models import MarkdownxField

class PublishedPostManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset() \
            .filter(is_published=True) \
            .order_by('-published_at')


class Post(models.Model):
    objects = models.Manager()
    published_objects = PublishedPostManager()

    is_published = models.BooleanField(default=False)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    excerpt = models.TextField()
    body = models.TextField()
    created_at = models.DateTimeField('date created', auto_now_add=True)
    updated_at = models.DateTimeField('last modified', auto_now=True)
    published_at = models.DateTimeField('date published', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('posts:detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title
