from django.contrib import admin

from .models import Restaurant


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "owner",
        "email",
        "phone_number",
        "average_rating",
        "delivery_time",
        "minimum_order",
        "delivery_fee",
        "is_active",
        "created_at",
    )

    list_filter = (
        "is_active",
        "created_at",
        "updated_at",
    )

    search_fields = (
        "name",
        "owner__username",
        "email",
        "phone_number",
        "address",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    ordering = (
        "-created_at",
    )