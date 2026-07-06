from rest_framework import serializers

from .models import Restaurant


class RestaurantSerializer(serializers.ModelSerializer):

    # Show category name when retrieving data
    category = serializers.StringRelatedField(read_only=True)

    # Accept category ID when creating/updating
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Restaurant._meta.get_field("category").remote_field.model.objects.all(),
        source="category",
        write_only=True
    )

    class Meta:

        model = Restaurant

        fields = [
            'id',
            'owner',
            'category',
            'category_id',
            'name',
            'description',
            'address',
            'phone_number',
            'image',
            'opening_time',
            'closing_time',
            'is_active',
            'created_at',
            'updated_at',
        ]

        read_only_fields = [
            'id',
            'owner',
            'created_at',
            'updated_at',
        ]