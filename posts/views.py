from django.http.request import HttpRequest
from django.shortcuts import render

from posts.models import Post


def post_list(request: HttpRequest):
    posts = Post.objects.all()  # SELECT * FROM posts;
    print(request.path)
    return render(request, "posts/list.html", context={"posts": posts})


def post_detail(r, pk):
    post = Post.objects.get(id=pk)  # SELECT * FROM posts WHERE id = ?;
    print(r.path)
    return render(r, "posts/detail.html", context={"post": post})
# def hello(r):
#     post = Post.objects.get(id=1)
#     return HttpResponse(f"Hello {post.title}!")

# def time(r):
#     dt = datetime.now()
#     return HttpResponse(f"NOW:{dt.strftime('%Y-%m-%d %H:%M:%S')}")

# def age(r):
#     age = 16
#     return HttpResponse(f"<h1>Onesim is {age} years old!</h1>")