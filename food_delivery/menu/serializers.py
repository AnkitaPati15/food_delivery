from rest_framework import serializers

from .models import Category, MenuItem


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'restaurant',
            'name',
            'created_at',
        ]


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = [
            'id',
            'restaurant',
            'category',
            'name',
            'description',
            'price',
            'image',
            'is_available',
            'created_at',
            'updated_at',
        ]
