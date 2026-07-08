from django.db import models

from accounts.models import User
from common.models import SoftDeleteModel
from .managers import RestaurantManager


class Restaurant(SoftDeleteModel):

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="restaurants",
    )

    name = models.CharField(
        max_length=255
    )

    description = models.TextField()

    address = models.TextField()

    phone_number = models.CharField(
        max_length=15
    )

    email = models.EmailField(
        blank=True,
        null=True,
    )

    website = models.URLField(
        blank=True,
        null=True,
    )

    logo = models.ImageField(
        upload_to="restaurant_logos/",
        blank=True,
        null=True,
    )

    cover_image = models.ImageField(
        upload_to="restaurant_covers/",
        blank=True,
        null=True,
    )

    delivery_time = models.PositiveIntegerField(
        default=30,
        help_text="Delivery time in minutes",
    )

    minimum_order = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0,
    )

    delivery_fee = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0,
    )

    average_rating = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        default=0,
    )

    opening_time = models.TimeField()

    closing_time = models.TimeField()

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    objects = RestaurantManager()

    def __str__(self):
        return self.name