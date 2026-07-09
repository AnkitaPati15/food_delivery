from django import forms

from .models import User
from django.contrib.auth.forms import PasswordChangeForm


class CustomPasswordChangeForm(PasswordChangeForm):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.fields["old_password"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Current Password",
            }
        )

        self.fields["new_password1"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "New Password",
            }
        )

        self.fields["new_password2"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Confirm New Password",
            }
        )


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