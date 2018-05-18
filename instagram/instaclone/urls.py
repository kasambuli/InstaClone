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
    url(r'^follow/(\d+)',views.follow,name="follow")
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
