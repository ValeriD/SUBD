from django.conf.urls import url
from ..views import member_views

urlpatterns= [
    url(r'^$', member_views.index, name='index'),
    url(r'^create$', member_views.create, name='create'),
    url(r'^edit/(?P<id>\d+)$', member_views.edit, name='edit'),
    url(r'^edit/update/(?P<id>\d+)$', member_views.update, name='update'),
    url(r'^delete/(?P<id>\d+)$', member_views.delete, name='delete'),
]
