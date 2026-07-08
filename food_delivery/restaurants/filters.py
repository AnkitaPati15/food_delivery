import django_filters
from .models import Restaurant


class RestaurantFilter(django_filters.FilterSet):
    """
    Filter for restaurants by name, rating, and is_active status.
    """

    name = django_filters.CharFilter(
        field_name="name", lookup_expr="icontains"
    )
    min_rating = django_filters.NumberFilter(
        field_name="average_rating", lookup_expr="gte"
    )
    max_rating = django_filters.NumberFilter(
        field_name="average_rating", lookup_expr="lte"
    )
    is_active = django_filters.BooleanFilter(field_name="is_active")

    class Meta:
        model = Restaurant
        fields = ["name", "min_rating", "max_rating", "is_active"]
