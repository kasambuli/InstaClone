from django import forms
from .models import Profile, Comments,Image
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# profile form
class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['comment']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar','name','bio','email']

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image','image_name','image_caption']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
