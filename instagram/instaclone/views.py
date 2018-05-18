from .forms import CommentsForm,ImageForm,ProfileForm,UserForm
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Profile,Image,Comments
from django.http import Http404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
# Create your views here.

@login_required(login_url='/accounts/login/')
def update_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            user = Profile.objects.get(user=current_user)
            profile.profile = user
            profile.user = current_user
            profile.save()
            return redirect('/')

    else:
        form = ProfileForm()

    return render(request, 'editprofile.html', {"form": form})

@login_required
def profile(request):
    current_user = request.user
    current_user.id = request.user.id
    try:
        profile = Profile.objects.get(user_id = current_user.id)
        image = Image.objects.filter(profile__user = current_user.id)

        return render(request, 'profile.html', {"profile":profile, "image": image})


    except ValueError:
        raise Http404()

def search_username(request):

    if 'name' in request.GET and request.GET["name"]:
        searched_name = request.GET.get("name")
        username = Profile.search_by_name(searched_name)
        message = f"{searched_name}"

        return render(request, 'search.html', {"message": message, "username": username})

    else:
        message = "Sorry, No one by this username"
        return render(request, 'search.html', {"message": message})


@login_required(login_url='/accounts/login/')
def index(request):
    current_user = request.user.id
    profile = Profile.objects.all()
    image = Image.display_images()
    comments = Comments.objects.all()
    
    return render(request,'index.html',{"image":image,"current_user":current_user,"profile":profile,"comments":comments})


def comment(request, image_id):
    current_user = request.user
    current_image = Image.objects.get(id=image_id)
    try:

        if request.method == 'POST':
            form = CommentsForm(request.POST, request.FILES)
            if form.is_valid():
                comment= form.save(commit=False)
                comment.user = current_user
                comment.image = current_image
                comment.save()
            
            return redirect('/')
        else:
                form = CommentsForm()

    except ValueError:
        Http404
    return render(request, 'comments.html', {"form": form, "current_image": current_image, id: image_id})


def viewImage(request, image_id):
    try:
        details = Image.objects.get(id=image_id)
    except DoesNotExist:
        raise Http404()
    images = Image.objects.get(id = image_id)
    comment = Comments.objects.filter(image= details)
    images.likes.filter(id = request.user.id)
    return render(request, 'image.html', {"comment": comment,"details": details, id: image_id,"likes":images.all_likes()})

def postImage(request):
    current_user = request.user
    Profile.objects.filter(user_id=current_user.id).exists()

    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            user = Profile.objects.get(user = current_user)
            image.profile = user
            image.user = current_user
            image.save()
            return redirect('/')

    else:
        form = ImageForm()

    return render(request, 'images.html', {"form": form})


def likes(request, image_id):
    image = Image.objects.get(id=image_id)
    
    if image.likes.filter(id=request.user.id).exists():
        image.likes.remove(request.user)

    else:
        image.likes.add(request.user,image.id)

    return redirect(viewImage,image.id)

def explore(request):

    image = Image.objects.all()
    comments = Comments.objects.all()

    return render(request,'explore.html',{"image":image,"comments":comments})
def follow(request,user_id):
    current_user =User.objects.get(id = user_id)
    follow = Profile.objects.get(id=request.user.id)

    if follow.follow.filter(id = user_id).exists():
        follow.follow.remove(current_user)
    else:
        follow.follow.add(current_user)

    return redirect(profile,current_user.id)
