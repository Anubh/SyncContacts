from django.conf.urls import patterns, url
from gmailacc import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'auth/google', views.redirectresp, name='redirectresp')
)
