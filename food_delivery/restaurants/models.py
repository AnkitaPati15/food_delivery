from django.db import models

from accounts.models import User


class Restaurant(models.Model):

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='restaurants'
    )

    name = models.CharField(
        max_length=255
    )

    description = models.TextField()

    address = models.TextField()

    phone_number = models.CharField(
        max_length=15
    )

    image = models.ImageField(
        upload_to='restaurant_images/',
        blank=True,
        null=True
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

    def __str__(self):

        return self.name