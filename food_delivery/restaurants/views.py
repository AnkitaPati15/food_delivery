from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from .models import Restaurant
from .serializers import RestaurantSerializer


class RestaurantListCreateView(generics.ListCreateAPIView):

    queryset = Restaurant.objects.all()

    serializer_class = RestaurantSerializer

    permission_classes = [IsAuthenticatedOrReadOnly]

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        restaurant = Restaurant.objects.create(
            owner=request.user,
            name=serializer.validated_data['name'],
            description=serializer.validated_data['description'],
            address=serializer.validated_data['address'],
            phone_number=serializer.validated_data['phone_number'],
            image=serializer.validated_data.get('image'),
            opening_time=serializer.validated_data['opening_time'],
            closing_time=serializer.validated_data['closing_time'],
        )

        return Response(
            RestaurantSerializer(restaurant).data,
            status=status.HTTP_201_CREATED
        )


class RestaurantDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Restaurant.objects.all()

    serializer_class = RestaurantSerializer

    permission_classes = [IsAuthenticatedOrReadOnly]