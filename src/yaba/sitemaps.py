from posts.models import Post
from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class PostsSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Post.published_objects.all()

    def lastmod(self, obj):
        return obj.published_at


class IndexViewSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 1

    def items(self):
        return ['posts:index']

    def location(self, obj):
        return reverse(obj)


class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'never'

    def items(self):
        return ['about', 'contact']

    def location(self, item):
        return reverse(item)
