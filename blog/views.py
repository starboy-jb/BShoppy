from django.shortcuts import render
from django.http import HttpResponse
from .models import BlogPost
# Create your views here.

def index(request):
    myPosts = BlogPost.objects.all()
    return render(request, 'blog/index.html', {'myPosts': myPosts})


def blogPost(request, id):
    post = BlogPost.objects.filter(post_id = id)[0]
    return render(request, 'blog/blogpost.html', {'post': post})