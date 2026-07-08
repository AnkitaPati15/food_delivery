from rest_framework import serializers

from .models import Restaurant


class RestaurantSerializer(serializers.ModelSerializer):

    owner = serializers.StringRelatedField(
        read_only=True
    )

    class Meta:

        model = Restaurant

        fields = [
            "id",
            "owner",
            "name",
            "description",
            "address",
            "phone_number",
            "email",
            "website",
            "logo",
            "cover_image",
            "delivery_time",
            "minimum_order",
            "delivery_fee",
            "average_rating",
            "opening_time",
            "closing_time",
            "is_active",
            "created_at",
            "updated_at",
            "is_deleted",
            "deleted_at",
        ]

        read_only_fields = [
            "id",
            "owner",
            "average_rating",
            "created_at",
            "updated_at",
            "is_deleted",
            "deleted_at",
        ]