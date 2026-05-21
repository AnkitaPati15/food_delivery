from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import (
    Cart,
    CartItem,
)

from .serializers import (
    CartSerializer,
    CartItemSerializer,
)

from menu.models import MenuItem


class CartView(generics.RetrieveAPIView):

    serializer_class = CartSerializer

    permission_classes = [IsAuthenticated]

    def get_object(self):

        cart, created = Cart.objects.get_or_create(
            user=self.request.user
        )

        return cart


class AddToCartView(generics.CreateAPIView):

    serializer_class = CartItemSerializer

    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):

        menu_item_id = request.data.get('menu_item')

        quantity = request.data.get('quantity', 1)

        menu_item = MenuItem.objects.get(
            id=menu_item_id
        )

        cart, created = Cart.objects.get_or_create(
            user=request.user
        )

        cart_item = CartItem.objects.create(
            cart=cart,
            menu_item=menu_item,
            quantity=quantity
        )

        return Response(
            CartItemSerializer(cart_item).data,
            status=status.HTTP_201_CREATED
        )


class CartItemDetailView(
    generics.RetrieveUpdateDestroyAPIView
):

    queryset = CartItem.objects.all()

    serializer_class = CartItemSerializer

    permission_classes = [IsAuthenticated]