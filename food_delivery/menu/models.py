from django.db import models

from restaurants.models import Restaurant


class Category(models.Model):

    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name='categories'
    )

    name = models.CharField(
        max_length=255
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name


class MenuItem(models.Model):

    FOOD_TYPE_CHOICES = [
        ("VEG", "Veg"),
        ("NON_VEG", "Non Veg"),
        ("EGG", "Egg"),
    ]

    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name='menu_items'
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='menu_items'
    )

    name = models.CharField(
        max_length=255
    )

    description = models.TextField()

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    discount_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )

    image = models.ImageField(
        upload_to='menu_items/',
        blank=True,
        null=True
    )

    food_type = models.CharField(
        max_length=10,
        choices=FOOD_TYPE_CHOICES,
        default="VEG"
    )

    preparation_time = models.PositiveIntegerField(
        default=20,
        help_text="Preparation time in minutes"
    )

    calories = models.PositiveIntegerField(
        blank=True,
        null=True
    )

    is_featured = models.BooleanField(
        default=False
    )

    is_available = models.BooleanField(
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