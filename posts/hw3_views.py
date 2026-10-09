from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.http import require_POST

from .models import Post


@require_POST
def toggle_post_active(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.is_active = not post.is_active
    post.save()
    return redirect("post_detail", pk=post.pk)