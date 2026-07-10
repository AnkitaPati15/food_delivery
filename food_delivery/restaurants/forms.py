from django import forms

from .models import Restaurant


class RestaurantForm(forms.ModelForm):

    class Meta:
        model = Restaurant

        fields = [
            "name",
            "description",
            "address",
            "phone_number",
            "email",
            "website",
            "logo",
            "cover_image",
            "delivery_time",
            "minimum_order",
            "delivery_fee",
            "opening_time",
            "closing_time",
            "is_active",
        ]

        widgets = {
            "description": forms.Textarea(attrs={"rows": 4}),
            "opening_time": forms.TimeInput(attrs={"type": "time"}),
            "closing_time": forms.TimeInput(attrs={"type": "time"}),
        }