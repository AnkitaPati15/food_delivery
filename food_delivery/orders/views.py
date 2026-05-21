from decimal import Decimal

from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import (
    Order,
    OrderItem,
)

from .serializers import (
    OrderSerializer,
)

from cart.models import (
    Cart,
    CartItem,
)


class OrderListCreateView(generics.ListCreateAPIView):

    serializer_class = OrderSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        return Order.objects.filter(
            user=self.request.user
        )

    def create(self, request, *args, **kwargs):

        delivery_address = request.data.get(
            'delivery_address'
        )

        cart = Cart.objects.get(
            user=request.user
        )

        cart_items = CartItem.objects.filter(
            cart=cart
        )

        total_amount = Decimal('0.00')

        order = Order.objects.create(
            user=request.user,
            delivery_address=delivery_address,
        )

        for cart_item in cart_items:

            item_total = (
                cart_item.menu_item.price *
                cart_item.quantity
            )

            total_amount += item_total

            OrderItem.objects.create(
                order=order,
                menu_item=cart_item.menu_item,
                quantity=cart_item.quantity,
                price=cart_item.menu_item.price
            )

        order.total_amount = total_amount

        order.save()

        cart_items.delete()

        return Response(
            OrderSerializer(order).data,
            status=status.HTTP_201_CREATED
        )


class OrderDetailView(
    generics.RetrieveUpdateAPIView
):

    queryset = Order.objects.all()

    serializer_class = OrderSerializer

    permission_classes = [IsAuthenticated]