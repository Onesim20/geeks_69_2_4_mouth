from django.views.generic import DetailView, ListView

from .models import Post


class ActivePostListView(ListView):
    # SELECT * FROM posts_post WHERE is_active = True;
    queryset = Post.objects.filter(is_active=True)
    template_name = "posts/list.html"      # шаблон из templates/ (как у учителя)
    context_object_name = "posts"


class ActivePostDetailView(DetailView):
    # неактивный пост по этому адресу даст 404
    queryset = Post.objects.filter(is_active=True)
    template_name = "posts/detail.html"
    context_object_name = "post"