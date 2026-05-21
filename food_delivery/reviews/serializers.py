from rest_framework import serializers

from .models import (
    RestaurantReview,
    MenuItemReview,
)


class RestaurantReviewSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = RestaurantReview

        fields = '__all__'

        read_only_fields = [
            'id',
            'user',
            'created_at',
            'updated_at',
        ]


class MenuItemReviewSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = MenuItemReview

        fields = '__all__'

        read_only_fields = [
            'id',
            'user',
            'created_at',
            'updated_at',
        ]