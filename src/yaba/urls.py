"""yaba URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.views.generic import TemplateView

from . import views
from .sitemaps import PostsSitemap, StaticViewSitemap, IndexViewSitemap

# Sitemaps
sitemaps = {
    'index': IndexViewSitemap,
    'posts': PostsSitemap,
    'static': StaticViewSitemap
}

urlpatterns = [
                  url(r'^admin/', admin.site.urls),
                  url(r'^about/', views.about, name='about'),
                  url(r'^contact/', views.contact, name='contact'),
                  url(r'^markdownx/', include('markdownx.urls')),
                  url(r'^404/$', TemplateView.as_view(template_name='yaba/../templates/404.html')),
                  url(r'^500/$', TemplateView.as_view(template_name='yaba/../templates/500.html')),
                  url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
                      name='django.contrib.sitemaps.views.sitemap'),
                  url(r'^', include('posts.urls'))
              ] \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
