"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from posts.views import create_post, post_detail, post_list
from posts.hw1_views import age, hello, hello_post, time
from posts.hw2_views import ActivePostDetailView, ActivePostListView
from posts.hw3_views import toggle_post_active
urlpatterns = [
    path("admin/", admin.site.urls),


    path("", post_list, name="post_list"),
    path("post/create/", create_post, name="create_post"),
    path("post/<int:pk>", post_detail, name="post_detail"),

    path("hello", hello, name="hello"),
    path("hello-post", hello_post, name="hello_post"),
    path("now", time, name="now"),
    path("age", age, name="age"),

    path("active/", ActivePostListView.as_view(), name="active_post_list"),
    path("active/<int:pk>/", ActivePostDetailView.as_view(), name="active_post_detail"),
    path("toggle-post-active/<int:pk>/", toggle_post_active, name="toggle_post_active"),
]

#
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)