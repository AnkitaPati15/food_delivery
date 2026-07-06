from django.contrib import admin

from .models import Category, MenuItem


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "restaurant",
        "created_at",
    )

    search_fields = (
        "name",
        "restaurant__name",
    )

    list_filter = (
        "restaurant",
    )


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "restaurant",
        "category",
        "price",
        "discount_price",
        "food_type",
        "is_available",
        "is_featured",
    )

    list_filter = (
        "restaurant",
        "category",
        "food_type",
        "is_available",
        "is_featured",
    )

    search_fields = (
        "name",
        "description",
        "restaurant__name",
    )

    list_editable = (
        "price",
        "discount_price",
        "is_available",
        "is_featured",
    )