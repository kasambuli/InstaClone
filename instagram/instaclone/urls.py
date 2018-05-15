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
    # url(r'^image/(\d+)/comment', views.comment, name='comment'), url(r'^likes/',views.likes,name = likes)
   
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
