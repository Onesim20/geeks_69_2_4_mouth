from django.contrib import admin

from .models import Category, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "user", "is_active")
    list_filter = ("is_active", "category")


admin.site.register(Category)