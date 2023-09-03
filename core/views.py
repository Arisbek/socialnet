from django.shortcuts import render, HttpResponse
from .models import *
# Create your views here.
def homepage(request):
    return render(request,"home.html")

def contacts(request):
    return HttpResponse("Наши контакты!")

def about_us(request):
    return HttpResponse("Информация о нас!")

def shorts(request):
    shorts = Short.objects.all()
    return render(request,"shorts.html",{'shorts':shorts})

def short_info(request,id):
    short = Short.objects.get(id=id)
    return render(request,"short.html",{'short':short})

def Categories(request):
    categories=Category.objects.all()
    return render(request,"categories.html",{'categories':categories})

def Category_info(request,id):
    category=Category.objects.get(id=id)
    return render(request,"category.html",{'category':category})

def posts(request):
    posts_list = Post.objects.all()
    return render(request,"posts.html",{'posts':posts_list})

def post_info(request,id):
    post = Post.objects.get(id=id)
    return render(request,"post.html", {'post':post})

# def savedposts(request):
#     posts=SavedPosts.objects.filter(saved_posts=request.user)
#     return render(request,"savedposts.html",{'posts':posts})

# def savedposts(request):
#     print(request.user)  # Print the user for debugging purposes
#     posts = SavedPosts.objects.filter(saved_posts=request.user)
#     print(len(posts))  # Print the number of SavedPosts records for this user
#     return render(request, "savedposts.html", {'posts': posts})

from django.contrib.auth.decorators import login_required  # Import the login_required decorator

# @login_required  # Decorate the view with login_required to ensure the user is logged in
def savedposts(request):
    # Filter SavedPosts by the currently logged-in user
    posts = SavedPosts.objects.filter(user=request.user)
    return render(request, "savedposts.html", {'posts': posts})


def comment(request):
    comment=Comment.objects.all()
    return render(request,"comment.html",{'comment':comment})

def profile(request, id):
    user = User.objects.get(id=id)
    posts = Post.objects.filter(creator=user)
    return render(request, 'profile.html', {'user':user, 'posts':posts})