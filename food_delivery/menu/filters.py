import django_filters
from .models import MenuItem


class MenuItemFilter(django_filters.FilterSet):
    """
    Filter for menu items by name, price range, and availability.
    """

    name = django_filters.CharFilter(
        field_name="name", lookup_expr="icontains"
    )
    min_price = django_filters.NumberFilter(
        field_name="price", lookup_expr="gte"
    )
    max_price = django_filters.NumberFilter(
        field_name="price", lookup_expr="lte"
    )
    is_available = django_filters.BooleanFilter(field_name="is_available")

    class Meta:
        model = MenuItem
        fields = ["name", "min_price", "max_price", "is_available"]
