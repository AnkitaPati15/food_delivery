from django import forms

from .models import Address


class AddressForm(forms.ModelForm):

    class Meta:

        model = Address

        fields = [
            "title",
            "full_address",
            "city",
            "state",
            "pincode",
            "landmark",
            "is_default",
        ]

        widgets = {

            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Home / Office",
                }
            ),

            "full_address": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                }
            ),

            "city": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),

            "state": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),

            "pincode": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),

            "landmark": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),

            "is_default": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),
        }