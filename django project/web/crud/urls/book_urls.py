from django.conf.urls import url
from ..views import book_views

urlpatterns= [
    url(r'^$', book_views.index, name='index'),
    url(r'^create$', book_views.create, name='create'),
    url(r'^edit/(?P<id>\d+)$', book_views.edit, name='edit'),
    url(r'^edit/update/(?P<id>\d+)$', book_views.update, name='update'),
    url(r'^delete/(?P<id>\d+)$', book_views.delete, name='delete'),
]
