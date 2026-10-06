from datetime import datetime

from django.http import HttpResponse

from .models import Post


def hello(request):
    post = Post.objects.first()
    if post is None:
        return HttpResponse("Постов пока нет")
    return HttpResponse(f"Hello {post.title}!")


def hello_post(request):
    # вывод всех полей модели Post: title, description, is_active
    post = Post.objects.first()
    if post is None:
        return HttpResponse("Постов пока нет")
    return HttpResponse(
        f"Title: {post.title}<br>"
        f"Description: {post.description}<br>"
        f"Active: {post.is_active}"
    )


def time(request):
    dt = datetime.now()
    return HttpResponse(f"NOW:{dt.strftime('%Y-%m-%d %H:%M:%S')}")


def age(request):
    age = 16
    return HttpResponse(f"<h1>Onesim is {age} years old!</h1>")