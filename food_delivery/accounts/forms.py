from django import forms

from .models import User


class ProfileUpdateForm(forms.ModelForm):

    class Meta:

        model = User

        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "profile_image",
        ]

        widgets = {

            "username": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),

            "first_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),

            "last_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),

            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                }
            ),

            "phone_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),

            "profile_image": forms.FileInput(
                attrs={
                    "class": "form-control",
                }
            ),
        }