import os

from django.db import models
from django.urls import reverse
from tagging.registry import register
from tagging.fields import TagField


def rename_file_with_slug(old_filename, slug):
    filename, file_extension = os.path.splitext(old_filename)
    truncated_slug = slug[:25] if len(slug) > 25 else slug
    return '{0}{1}'.format(truncated_slug, file_extension)


def generate_featured_image_path(instance, filename):
    return 'posts/uploads/{0}'.format(rename_file_with_slug(filename, instance.slug))


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
    slug = models.SlugField(max_length=50, unique=True)
    excerpt = models.TextField()
    body = models.TextField()
    tags = TagField()
    featured_image = models.ImageField(upload_to=generate_featured_image_path, null=True)
    created_at = models.DateTimeField('date created', auto_now_add=True)
    updated_at = models.DateTimeField('last modified', auto_now=True)
    published_at = models.DateTimeField('date published', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('posts:detail', kwargs={'slug': self.slug})

    def get_others(self):
        return Post.published_objects.exclude(pk=self.pk)

    def get_next_published(self):
        try:
            published_gte = self.get_others().filter(published_at__gte=self.published_at)
            return published_gte.order_by('published_at')[0]
        except IndexError:
            raise Post.DoesNotExist

    def get_previous_published(self):
        try:
            published_lte = self.get_others().filter(published_at__lte=self.published_at)
            return published_lte.order_by('-published_at')[0]
        except IndexError:
            raise Post.DoesNotExist

    def __str__(self):
        return self.title


register(Post, 'post_tags')
