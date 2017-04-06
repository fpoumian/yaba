from django.conf.urls import url
from tagging.views import TaggedObjectList
from .models import Post

from . import views

app_name = 'posts'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^posts/$', views.list, name='list'),
    url(r'^posts/(?P<slug>[\w-]+)/$', views.detail, name='detail'),
    url(r'^posts/tag/(?P<tag>[^/]+(?u))/$',
        views.TaggedPostsList.as_view(),
        name='tag')
]
