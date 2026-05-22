from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

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

    queryset = RestaurantReview.objects.all()

    serializer_class = RestaurantReviewSerializer

    permission_classes = [IsAuthenticatedOrReadOnly]

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(
            data=request.data
        )

        serializer.is_valid(raise_exception=True)

        review = RestaurantReview.objects.create(
            user=request.user,
            restaurant=serializer.validated_data[
                'restaurant'
            ],
            rating=serializer.validated_data[
                'rating'
            ],
            comment=serializer.validated_data[
                'comment'
            ],
        )

        return Response(
            RestaurantReviewSerializer(review).data,
            status=status.HTTP_201_CREATED
        )


class RestaurantReviewDetailView(
    generics.RetrieveUpdateDestroyAPIView
):

    queryset = RestaurantReview.objects.all()

    serializer_class = RestaurantReviewSerializer

    permission_classes = [IsAuthenticatedOrReadOnly]


class MenuItemReviewListCreateView(
    generics.ListCreateAPIView
):

    queryset = MenuItemReview.objects.all()

    serializer_class = MenuItemReviewSerializer

    permission_classes = [IsAuthenticatedOrReadOnly]

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(
            data=request.data
        )

        serializer.is_valid(raise_exception=True)

        review = MenuItemReview.objects.create(
            user=request.user,
            menu_item=serializer.validated_data[
                'menu_item'
            ],
            rating=serializer.validated_data[
                'rating'
            ],
            comment=serializer.validated_data[
                'comment'
            ],
        )

        return Response(
            MenuItemReviewSerializer(review).data,
            status=status.HTTP_201_CREATED
        )


class MenuItemReviewDetailView(
    generics.RetrieveUpdateDestroyAPIView
):

    queryset = MenuItemReview.objects.all()

    serializer_class = MenuItemReviewSerializer

    permission_classes = [IsAuthenticatedOrReadOnly]