from django.shortcuts import render, redirect
from .models import UserBio, UserPost, UserProfile
from .forms import UserProfileForm, UserBioForm, UserPostForm
from django.http import HttpResponse

def index(request):
    title = 'welcome'
    return render(request,'mytemplates/index.html',{'title':title})

def profile(request):
    form = UserProfileForm()
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES,
                               instance=request.user.userprofile)
        if form.is_valid():
            print('valid')
            form.save()
            print('save')
    return render(request, 'mytemplates/profile.html', {'form': form, 'title': 'userprofile'})


def bio(request):
    form = UserBioForm(instance=request.user.userbio)
    if request.method == "POST":
        form = UserBioForm(request.POST, instance=request.user.userbio)
        if form.is_valid():
            form.save()
            print('saved')
    return render(request, 'mytemplates/bio.html', {'form': form, 'title': 'userbio'})


def post(request):
    form = UserPostForm()
    user = request.user
    if request.method == "POST":
        form = UserPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = user.userpost_set.create(title=form.cleaned_data['title'],
                                            image=form.cleaned_data['image'])
            post.save()
            return redirect('mypost')
        else:
            print('not valid')
    return render(request, 'mytemplates/post.html', {'form': form, 'title': 'post'})


def my_post(request):
    user = request.user
    posts = user.userpost_set.all()
    print(user.username)
    return render(request, 'mytemplates/mypost.html', {'posts': posts, 'title': 'userbio'})


def del_my_post(request, pk):
    del_post = UserPost.objects.get(id=pk)
    del_post.delete()
    return redirect(request.META['HTTP_REFERER'])


def all_post(request):
    total_post = UserPost.objects.all()
    return render(request, 'mytemplates/allpost.html', {'total_post': total_post, 'title': 'allpost'})
