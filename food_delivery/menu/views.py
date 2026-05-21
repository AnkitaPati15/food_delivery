from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import (
    Category,
    MenuItem,
)

from .serializers import (
    CategorySerializer,
    MenuItemSerializer,
)


class CategoryListCreateView(generics.ListCreateAPIView):

    queryset = Category.objects.all()

    serializer_class = CategorySerializer

    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        category = Category.objects.create(
            restaurant=serializer.validated_data['restaurant'],
            name=serializer.validated_data['name'],
        )

        return Response(
            CategorySerializer(category).data,
            status=status.HTTP_201_CREATED
        )


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Category.objects.all()

    serializer_class = CategorySerializer

    permission_classes = [IsAuthenticated]


class MenuItemListCreateView(generics.ListCreateAPIView):

    queryset = MenuItem.objects.all()

    serializer_class = MenuItemSerializer

    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        menu_item = MenuItem.objects.create(
            restaurant=serializer.validated_data['restaurant'],
            category=serializer.validated_data['category'],
            name=serializer.validated_data['name'],
            description=serializer.validated_data['description'],
            price=serializer.validated_data['price'],
            image=serializer.validated_data.get('image'),
            is_available=serializer.validated_data.get(
                'is_available',
                True
            ),
        )

        return Response(
            MenuItemSerializer(menu_item).data,
            status=status.HTTP_201_CREATED
        )


class MenuItemDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = MenuItem.objects.all()

    serializer_class = MenuItemSerializer

    permission_classes = [IsAuthenticated]