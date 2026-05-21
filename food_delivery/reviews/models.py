from django.db import models

from accounts.models import User
from restaurants.models import Restaurant
from menu.models import MenuItem


class RestaurantReview(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='restaurant_reviews'
    )

    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name='reviews'
    )

    rating = models.PositiveIntegerField()

    comment = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):

        return f"{self.restaurant.name} Review"


class MenuItemReview(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='menu_reviews'
    )

    menu_item = models.ForeignKey(
        MenuItem,
        on_delete=models.CASCADE,
        related_name='reviews'
    )

    rating = models.PositiveIntegerField()

    comment = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):

        return self.menu_item.name