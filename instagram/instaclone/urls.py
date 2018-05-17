from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search/', views.search_username, name='search_name'),
    url(r'^accounts/profile/', views.profile, name='profile'),
    url(r'^profile/', views.update_profile, name='editProfile'),
    url(r'^images/', views.postImage, name='postImage'),
    url(r'^image/(\d+)', views.viewImage, name='viewImage'),
    url(r'^likes/(\d+)',views.likes, name='likes'),
    url(r'^explore/',views.explore,name = 'explore'),
    url(r'^comment/(\d+)', views.comment, name='comment'), 
   
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views
