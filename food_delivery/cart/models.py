from django.db import models

from accounts.models import User
from menu.models import MenuItem


class Cart(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='cart'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):

        return f"{self.user.username} Cart"


class CartItem(models.Model):

    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name='items'
    )

    menu_item = models.ForeignKey(
        MenuItem,
        on_delete=models.CASCADE
    )

    quantity = models.PositiveIntegerField(
        default=1
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):

        return self.menu_item.name