from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from posts.forms import PostForm
from posts.models import Category, Post
from posts.services import get_by_filter



class PostListView(ListView):
    model = Post
    template_name = "posts/list.html"
    context_object_name = "posts"

   
    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get("search")

      
        return get_by_filter(queryset, search=search, name="islam")



class PostDetailView(DetailView):
    model = Post
    template_name = "posts/detail.html"
    pk_url_kwarg = "id"  



class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
   
    template_name = "posts/create.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
       
        context["categories"] = Category.objects.all()
        return context



class UpdatePostView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = "posts/edit.html"

    def get_object(self, queryset=None):
        post = super().get_object(queryset)
        if self.request.user != post.user:
            raise PermissionDenied()
        return post



class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = "posts/delete.html"
    success_url = reverse_lazy("l7_post_list")

  
    def get_object(self, queryset=None):
        post = super().get_object(queryset)
        if self.request.user != post.user:
            raise PermissionDenied()
        return post