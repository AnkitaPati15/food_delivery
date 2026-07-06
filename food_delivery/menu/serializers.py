from rest_framework import serializers

from .models import Category, MenuItem
from restaurants.models import Restaurant


class CategorySerializer(serializers.ModelSerializer):

    restaurant = serializers.StringRelatedField(read_only=True)

    restaurant_id = serializers.PrimaryKeyRelatedField(
        queryset=Restaurant.objects.all(),
        source="restaurant",
        write_only=True
    )

    class Meta:
        model = Category
        fields = [
            "id",
            "restaurant",
            "restaurant_id",
            "name",
            "created_at",
        ]
        read_only_fields = [
            "id",
            "created_at",
        ]


class MenuItemSerializer(serializers.ModelSerializer):

    restaurant = serializers.StringRelatedField(read_only=True)

    restaurant_id = serializers.PrimaryKeyRelatedField(
        queryset=Restaurant.objects.all(),
        source="restaurant",
        write_only=True
    )

    category = serializers.StringRelatedField(read_only=True)

    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source="category",
        write_only=True
    )

    class Meta:
        model = MenuItem
        fields = [
            "id",
            "restaurant",
            "restaurant_id",
            "category",
            "category_id",
            "name",
            "description",
            "price",
            "discount_price",
            "image",
            "food_type",
            "preparation_time",
            "calories",
            "is_featured",
            "is_available",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
        ]