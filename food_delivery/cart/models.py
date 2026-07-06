from decimal import Decimal

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

    @property
    def total_items(self):
        return sum(item.quantity for item in self.items.all())

    @property
    def total_price(self):
        total = Decimal("0.00")
        for item in self.items.all():
            total += item.subtotal
        return total


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

    class Meta:
        unique_together = ("cart", "menu_item")

    def __str__(self):
        return f"{self.menu_item.name} x {self.quantity}"

    @property
    def unit_price(self):
        if self.menu_item.discount_price:
            return self.menu_item.discount_price
        return self.menu_item.price

    @property
    def subtotal(self):
        return self.unit_price * self.quantity