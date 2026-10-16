from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Post


@login_required
def my_posts(request):
    posts = Post.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "posts/my_posts.html", {"posts": posts})