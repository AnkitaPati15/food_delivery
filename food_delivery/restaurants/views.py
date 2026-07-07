from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import generics, filters
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)

from .models import Restaurant
from .serializers import RestaurantSerializer


class RestaurantListCreateView(generics.ListCreateAPIView):

    serializer_class = RestaurantSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    filterset_fields = [
        "category",
        "is_active",
    ]

    search_fields = [
        "name",
        "description",
        "address",
    ]

    ordering_fields = [
        "name",
        "created_at",
        "delivery_time",
        "minimum_order",
        "delivery_fee",
    ]

    ordering = [
        "name",
    ]

    def get_permissions(self):

        if self.request.method == "POST":
            return [IsAuthenticated()]

        return [IsAuthenticatedOrReadOnly()]

    def get_queryset(self):

        queryset = Restaurant.objects.filter(
            is_active=True
        )

        category = self.request.query_params.get("category")

        if category:
            queryset = queryset.filter(
                category_id=category
            )

        return queryset

    def perform_create(self, serializer):

        if self.request.user.role != "restaurant_owner":

            raise PermissionError(
                "Only restaurant owners can create restaurants."
            )

        serializer.save(
            owner=self.request.user
        )


class RestaurantDetailView(
    generics.RetrieveUpdateDestroyAPIView
):

    serializer_class = RestaurantSerializer

    permission_classes = [
        IsAuthenticatedOrReadOnly
    ]

    def get_queryset(self):

        if self.request.method in [
            "PUT",
            "PATCH",
            "DELETE",
        ]:

            if not self.request.user.is_authenticated:
                return Restaurant.objects.none()

            if self.request.user.is_superuser:
                return Restaurant.objects.all()

            return Restaurant.objects.filter(
                owner=self.request.user
            )

        return Restaurant.objects.filter(
            is_active=True
        )