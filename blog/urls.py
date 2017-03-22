from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.post_list, name = 'post_list'),
    url(r'^sample.html', views.where_is_my_sample, name = 'sample'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
]