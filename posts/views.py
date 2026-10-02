from django.shortcuts import render
from django.http.response import HttpResponse
from datetime import datetime
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
    context_object_name = 'post'

def hello(r):
    post = Post.objects.first()
    if post is None:
        return HttpResponse("Постов пока нет")
    return HttpResponse(
        f"Title: {post.title}<br>"
        f"Description: {post.description}<br>"
        f"Active: {post.is_active}"
    )

def hello(r):
    post = Post.objects.get(id=1)
    return HttpResponse(f"Hello {post.title}!")

def time(r):
    dt = datetime.now()
    return HttpResponse(f"NOW:{dt.strftime('%Y-%m-%d %H:%M:%S')}")

def age(r):
    age = 16
    return HttpResponse(f"<h1>Onesim is {age} years old!</h1>")