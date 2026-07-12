from django import forms

from .models import Category, MenuItem


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
class MenuItemForm(forms.ModelForm):

    class Meta:

        model = MenuItem

        fields = [
            "restaurant",
            "category",
            "name",
            "description",
            "price",
            "discount_price",
            "image",
            "food_type",
            "preparation_time",
            "calories",
            "is_featured",
            "is_available",
        ]

        widgets = {

            "restaurant": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "category": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                }
            ),

            "price": forms.NumberInput(
                attrs={
                    "class": "form-control",
                }
            ),

            "discount_price": forms.NumberInput(
                attrs={
                    "class": "form-control",
                }
            ),

            "image": forms.FileInput(
                attrs={
                    "class": "form-control",
                }
            ),

            "food_type": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "preparation_time": forms.NumberInput(
                attrs={
                    "class": "form-control",
                }
            ),

            "calories": forms.NumberInput(
                attrs={
                    "class": "form-control",
                }
            ),
        }
