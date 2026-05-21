from django.db import models

from orders.models import Order


class Payment(models.Model):

    PAYMENT_METHOD_CHOICES = (
        ('cod', 'Cash On Delivery'),
    )

    PAYMENT_STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('failed', 'Failed'),
    )

    order = models.OneToOneField(
        Order,
        on_delete=models.CASCADE,
        related_name='payment'
    )

    payment_method = models.CharField(
        max_length=30,
        choices=PAYMENT_METHOD_CHOICES
    )

    payment_status = models.CharField(
        max_length=30,
        choices=PAYMENT_STATUS_CHOICES,
        default='pending'
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    transaction_id = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):

        return f"Payment {self.id}"