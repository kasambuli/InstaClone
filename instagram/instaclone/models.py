from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(blank = True,max_length = 30)
    bio = models.TextField(max_length=100)
    avatar = models.ImageField(upload_to = 'avatar/')


class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    image_name = models.CharField(blank = True, max_length = 30)
    image_caption = models.CharField(blank = True, max_length = 500)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    likes = models.IntegerField(default = 0)
    posted = models.DateTimeField(auto_now_add=True)

class Comments(models.Model):
    comment = models.TextField(blank = True, max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    posted = models.DateTimeField(auto_now_add=True)
