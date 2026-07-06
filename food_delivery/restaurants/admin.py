from django.contrib import admin
from .models import Restaurant, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "category",
        "owner",
        "delivery_time",
        "delivery_fee",
        "minimum_order",
        "is_active",
    )

    list_filter = (
        "category",
        "is_active",
    )

    search_fields = (
        "name",
        "address",
    )