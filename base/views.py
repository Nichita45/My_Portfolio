# Thank you for inspecting my code, which means I got the chance I wanted

from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from .forms import SignUpForm, LoginForm, PostForm, UserForm
from .models import Post
def home(request):
    return render(request, 'home.html')

def profile(request, id):
    user = User.objects.get(pk=id)
    context = {
        'user': user
    }
    return render(request, 'profile.html', context)

def about(request):
    return render(request, 'about.html')


# Posts section

def post(request, id):
    post = Post.objects.get(pk=id)
    count = Post.objects.count()
    num1 = count - 2
    p = Post.objects.all()[num1:count]
    context = {
        'post': post,
        'p': p
    }
    return render(request, 'posts/post.html', context)

def posts(request):
    post_list = Post.objects.all().order_by('?')
    p = Paginator(Post.objects.all(), 2)
    page = request.GET.get('page')
    posts = p.get_page(page)
    context = {
	    'posts': posts,
        'post_list': post_list
    }
    return render(request, 'posts/posts.html', context)


def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            instance.uploader = request.user
            instance.save()
            return redirect('home')
    else:
        form = PostForm()
    context = {
        'form': form
    }
    return render(request, 'posts/create_post.html', context)

def edit_post(request, id):
    post = Post.objects.get(pk=id)
    form = PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form': form
    }
    return render(request, 'posts/edit_post.html', context)


def delete_post(request, id):
    post = Post.objects.get(pk=id)
    if request.method == 'POST':
        post.delete()
        return redirect('home')
    context = {
        'post': post
    }
    return render(request, 'posts/delete_post.html', context)

# Auth section

def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    context = {
        'form': form
    }
    return render(request, 'auth/signup.html', context)

def logout_user(request):
    logout(request)
    return redirect('home')

def login_user(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = LoginForm(data=request.POST)
    context = {
        'form': form
    }
    return render(request, 'auth/login.html', context)

