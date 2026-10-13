from django import forms

from .models import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ("title",)
        labels = {"title": "Название категории"}
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control form-control-lg", "placeholder": "Например: Новости"}
            ),
        }
