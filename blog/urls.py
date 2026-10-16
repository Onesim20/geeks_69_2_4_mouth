from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from posts.views import create_post, delete_post, edit_post, post_detail, post_list
from user.views import register
from posts.hw1_views import age, hello, hello_post, time
from posts.hw2_views import ActivePostDetailView, ActivePostListView
from posts.hw3_views import toggle_post_active
from posts.hw4_views import create_category
from posts.hw5_views import my_posts

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login", auth_views.LoginView.as_view(), name="login"),
    path("logout", auth_views.LogoutView.as_view(), name="logout"),
    path("register", register, name="register"),
    path("", post_list, name="post_list"),
    path("post/create/", create_post, name="create_post"),
    path("post/<int:pk>/edit", edit_post, name="edit_post"),
    path("post/<int:pk>/delete", delete_post, name="delete_post"),
    path("post/<int:pk>", post_detail, name="post_detail"),


    path("hello", hello, name="hello"),
    path("hello-post", hello_post, name="hello_post"),
    path("now", time, name="now"),
    path("age", age, name="age"),

    path("active/", ActivePostListView.as_view(), name="active_post_list"),
    path("active/<int:pk>/", ActivePostDetailView.as_view(), name="active_post_detail"),

    path("toggle-post-active/<int:pk>/", toggle_post_active, name="toggle_post_active"),
    path("category/create/", create_category, name="create_category"),


    path("my-posts/", my_posts, name="my_posts"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)