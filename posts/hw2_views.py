from django.views.generic import DetailView, ListView

from .models import Post


class ActivePostListView(ListView):
  
    queryset = Post.objects.filter(is_active=True)
    template_name = "posts/list.html"      
    context_object_name = "posts"


class ActivePostDetailView(DetailView):

    queryset = Post.objects.filter(is_active=True)
    template_name = "posts/detail.html"
    context_object_name = "post"
