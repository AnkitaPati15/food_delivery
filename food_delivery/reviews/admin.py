from django.contrib import admin

from .models import (
    RestaurantReview,
    MenuItemReview,
)


admin.site.register(RestaurantReview)
admin.site.register(MenuItemReview)