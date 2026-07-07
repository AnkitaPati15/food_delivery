from rest_framework import generics
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)

from accounts.permissions import (
    IsCustomer,
)

from .models import (
    RestaurantReview,
    MenuItemReview,
)

from .serializers import (
    RestaurantReviewSerializer,
    MenuItemReviewSerializer,
)


class RestaurantReviewListCreateView(
    generics.ListCreateAPIView
):

    serializer_class = RestaurantReviewSerializer

    queryset = RestaurantReview.objects.all()

    permission_classes = [
        IsAuthenticatedOrReadOnly
    ]

    def get_permissions(self):

        if self.request.method == "POST":
            return [
                IsAuthenticated(),
                IsCustomer(),
            ]

        return [
            IsAuthenticatedOrReadOnly(),
        ]

    def perform_create(self, serializer):

        serializer.save(
            user=self.request.user
        )


class RestaurantReviewDetailView(
    generics.RetrieveUpdateDestroyAPIView
):

    serializer_class = RestaurantReviewSerializer

    permission_classes = [
        IsAuthenticatedOrReadOnly
    ]

    def get_queryset(self):

        if self.request.user.is_authenticated:

            if self.request.user.is_staff:
                return RestaurantReview.objects.all()

            return RestaurantReview.objects.filter(
                user=self.request.user
            )

        return RestaurantReview.objects.all()


class MenuItemReviewListCreateView(
    generics.ListCreateAPIView
):

    serializer_class = MenuItemReviewSerializer

    queryset = MenuItemReview.objects.all()

    permission_classes = [
        IsAuthenticatedOrReadOnly
    ]

    def get_permissions(self):

        if self.request.method == "POST":
            return [
                IsAuthenticated(),
                IsCustomer(),
            ]

        return [
            IsAuthenticatedOrReadOnly(),
        ]

    def perform_create(self, serializer):

        serializer.save(
            user=self.request.user
        )


class MenuItemReviewDetailView(
    generics.RetrieveUpdateDestroyAPIView
):

    serializer_class = MenuItemReviewSerializer

    permission_classes = [
        IsAuthenticatedOrReadOnly
    ]

    def get_queryset(self):

        if self.request.user.is_authenticated:

            if self.request.user.is_staff:
                return MenuItemReview.objects.all()

            return MenuItemReview.objects.filter(
                user=self.request.user
            )

        return MenuItemReview.objects.all()