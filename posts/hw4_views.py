from django.shortcuts import redirect, render

from .hw4_forms import CategoryForm


def create_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("create_post")  
    else:
        form = CategoryForm()
    return render(request, "posts/category_create.html", {"form": form})