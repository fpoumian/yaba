from django.db import models


class Post(models.Model):
    is_published = models.BooleanField(default=False)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    excerpt = models.TextField()
    body = models.TextField()
    created_at = models.DateTimeField('date created', auto_now_add=True)
    updated_at = models.DateTimeField('last modified', auto_now=True)
    published_at = models.DateTimeField('date published', null=True, blank=True)

    def __str__(self):
        return self.title
