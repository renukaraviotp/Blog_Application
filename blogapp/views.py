from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from blogapp.models import Post
from django.contrib import messages
from datetime import datetime

# home page
def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})

# login & signup page
def loginregister(request):
    return render(request, 'signuplogin.html')

# user home page
def userhome(request):
    return render(request, 'userhome.html')

# sign up function
def signupaction(request):
  if request.method=='POST':
    fname = request.POST.get('fname')
    lname = request.POST.get('lname')
    uname = request.POST.get('uname')
    pas = request.POST.get('pas')
    cpas = request.POST.get('cpas')
    email = request.POST.get('email')

    if pas != cpas:
        messages.error(request, 'Passwords do not match')
        return redirect('loginregister')
    
    if User.objects.filter(username=uname).exists():
        messages.error(request, 'Username is already taken')
        return redirect('loginregister')
    
    usr = User.objects.create_user(first_name=fname, last_name=lname, password=pas, email=email, username=uname)
    usr.save()
    messages.success(request, 'Account created successfully, please log in')
    return redirect('loginregister')

# login function
def loginaction(request):
  if request.method=='POST':
    username = request.POST.get('uname')
    password = request.POST.get('pas')
    user = auth.authenticate(username=username, password=password)
    
    if user is not None:
        auth.login(request, user)
        return redirect('userhome')  
    else:
        messages.error(request, 'Invalid username or password')
        return redirect('loginregister')

# logout function
@login_required(login_url='home')
def logoutt(request):
    logout(request)
    return redirect('home') 

# blog posts list
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})


# blog post creation
@login_required(login_url='loginregister')
def post_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        if title and content:
            created_at = datetime.now()  # Get current datetime for created_at field
            updated_at = created_at  # Initially, updated_at will be the same as created_at
            post = Post.objects.create(
                title=title,
                content=content,
                author=request.user,
                created_at=created_at,
                updated_at=updated_at
            )
            return redirect('post_list')  # Redirect to the post list page after saving
    return render(request, 'post_create.html')


# blog post details
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})

# update blog post
@login_required(login_url='home')
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)

    # Ensure the user is the author of the post
    if request.user != post.author:
        messages.error(request, "You are not authorized to update this post.")
        return redirect('post_list')

    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        if title and content:
            post.title = title
            post.content = content
            post.save() 
            return redirect('post_detail', pk=post.pk)
    
    return render(request, 'post_update.html', {'post': post})

# blog post delete
@login_required(login_url='home')
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)

    # Ensure the user is the author of the post
    if request.user != post.author:
        messages.error(request, "You are not authorized to delete this post.")
        return redirect('post_list')

    if request.method == 'POST':
        post.delete()
        messages.success(request, "Post deleted successfully.")
        return redirect('post_list')

    return render(request, 'confirm_delete.html', {'post': post})
       