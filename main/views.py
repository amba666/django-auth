from django.shortcuts import render, redirect 
from .forms import RegistrationForm , PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .models import Post
# auth

@login_required(login_url="login")
def home(request):
    posts = Post.objects.all()

    if request.method == "POST":
        post_id = request.POST.get("post-id")
        post = Post.objects.filter(id=post_id).first()
        if post and post.author == request.user:
            post.delete()

    return render(request,"main/index.html", {
        "posts":posts
    }) 

def sign_up(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')

    else:
        form = RegistrationForm()

    return render(request, "registration/sign_up.html", {
      "form": form   
    })

def password_change(request):
    return render(request, "registration/password_change")

#Post
@login_required(login_url="login")
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("home")
    else:
        form = PostForm()
    
    return render(request, 'main/create_post.html', {
        "form":form
    })