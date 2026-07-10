from django import forms

from .models import Category


class CategoryForm(forms.ModelForm):

    class Meta:

        model = Category

        fields = [
            "restaurant",
            "name",
        ]

        widgets = {

            "restaurant": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Category Name",
                }
            ),

        }