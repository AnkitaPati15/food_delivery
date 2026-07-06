from rest_framework import serializers

from .models import (
    Cart,
    CartItem,
)


class CartItemSerializer(serializers.ModelSerializer):

    menu_name = serializers.CharField(
        source="menu_item.name",
        read_only=True
    )

    unit_price = serializers.DecimalField(
        source="unit_price",
        max_digits=10,
        decimal_places=2,
        read_only=True
    )

    subtotal = serializers.DecimalField(
        source="subtotal",
        max_digits=10,
        decimal_places=2,
        read_only=True
    )

    class Meta:

        model = CartItem

        fields = [
            "id",
            "cart",
            "menu_item",
            "menu_name",
            "quantity",
            "unit_price",
            "subtotal",
            "created_at",
            "updated_at",
        ]

        read_only_fields = (
            "id",
            "created_at",
            "updated_at",
        )


class CartSerializer(serializers.ModelSerializer):

    items = CartItemSerializer(
        many=True,
        read_only=True
    )

    total_items = serializers.IntegerField(
        read_only=True
    )

    total_price = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
        read_only=True
    )

    class Meta:

        model = Cart

        fields = [
            "id",
            "user",
            "items",
            "total_items",
            "total_price",
            "created_at",
            "updated_at",
        ]

        read_only_fields = (
            "id",
            "user",
            "created_at",
            "updated_at",
        )