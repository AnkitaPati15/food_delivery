from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from .models import Restaurant
from .serializers import RestaurantSerializer


class RestaurantListCreateView(generics.ListCreateAPIView):

    queryset = Restaurant.objects.filter(is_active=True)

    serializer_class = RestaurantSerializer

    permission_classes = [IsAuthenticatedOrReadOnly]

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
    ]

    ordering = [
        "name",
    ]

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        restaurant = Restaurant.objects.create(
            owner=request.user,
            category=serializer.validated_data["category"],
            name=serializer.validated_data["name"],
            description=serializer.validated_data["description"],
            address=serializer.validated_data["address"],
            phone_number=serializer.validated_data["phone_number"],
            email=serializer.validated_data.get("email"),
            website=serializer.validated_data.get("website"),
            logo=serializer.validated_data.get("logo"),
            cover_image=serializer.validated_data.get("cover_image"),
            delivery_time=serializer.validated_data.get("delivery_time", 30),
            minimum_order=serializer.validated_data.get("minimum_order", 0),
            delivery_fee=serializer.validated_data.get("delivery_fee", 0),
            opening_time=serializer.validated_data["opening_time"],
            closing_time=serializer.validated_data["closing_time"],
)

        return Response(
            RestaurantSerializer(restaurant).data,
            status=status.HTTP_201_CREATED,
        )


class RestaurantDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Restaurant.objects.all()

    serializer_class = RestaurantSerializer

    permission_classes = [IsAuthenticatedOrReadOnly]