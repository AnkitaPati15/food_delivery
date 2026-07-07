from rest_framework import generics, status
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from rest_framework.response import Response

from accounts.permissions import (
    IsRestaurantOwnerOrAdmin,
)

from restaurants.models import Restaurant

from .models import (
    Category,
    MenuItem,
)

from .serializers import (
    CategorySerializer,
    MenuItemSerializer,
)


class CategoryListCreateView(generics.ListCreateAPIView):

    serializer_class = CategorySerializer

    queryset = Category.objects.all()

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_permissions(self):

        if self.request.method == "POST":
            return [
                IsAuthenticated(),
                IsRestaurantOwnerOrAdmin(),
            ]

        return [
            IsAuthenticatedOrReadOnly(),
        ]

    def perform_create(self, serializer):

        restaurant = serializer.validated_data["restaurant"]

        if (
            not self.request.user.is_staff
            and restaurant.owner != self.request.user
        ):
            raise PermissionError(
                "You can only add categories to your own restaurant."
            )

        serializer.save()


class CategoryDetailView(
    generics.RetrieveUpdateDestroyAPIView
):

    serializer_class = CategorySerializer

    permission_classes = [
        IsAuthenticatedOrReadOnly
    ]

    def get_queryset(self):

        if self.request.user.is_authenticated:

            if self.request.user.is_staff:
                return Category.objects.all()

            return Category.objects.filter(
                restaurant__owner=self.request.user
            )

        return Category.objects.all()


class MenuItemListCreateView(generics.ListCreateAPIView):

    serializer_class = MenuItemSerializer

    queryset = MenuItem.objects.all()

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_permissions(self):

        if self.request.method == "POST":
            return [
                IsAuthenticated(),
                IsRestaurantOwnerOrAdmin(),
            ]

        return [
            IsAuthenticatedOrReadOnly(),
        ]

    def perform_create(self, serializer):

        restaurant = serializer.validated_data["restaurant"]

        if (
            not self.request.user.is_staff
            and restaurant.owner != self.request.user
        ):
            raise PermissionError(
                "You can only add menu items to your own restaurant."
            )

        serializer.save()


class MenuItemDetailView(
    generics.RetrieveUpdateDestroyAPIView
):

    serializer_class = MenuItemSerializer

    permission_classes = [
        IsAuthenticatedOrReadOnly
    ]

    def get_queryset(self):

        if self.request.user.is_authenticated:

            if self.request.user.is_staff:
                return MenuItem.objects.all()

            return MenuItem.objects.filter(
                restaurant__owner=self.request.user
            )

        return MenuItem.objects.filter(
            is_available=True
        )