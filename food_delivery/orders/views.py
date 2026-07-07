from decimal import Decimal

from django.db import transaction
from django.db.models import Q

from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from cart.models import Cart, CartItem

from .models import Order, OrderItem
from .serializers import OrderSerializer


class OrderListCreateView(generics.ListCreateAPIView):

    serializer_class = OrderSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        user = self.request.user

        if user.is_staff:
            return Order.objects.all().order_by("-created_at")

        if user.role == "restaurant_owner":

            return (
                Order.objects.filter(
                    items__menu_item__restaurant__owner=user
                )
                .distinct()
                .order_by("-created_at")
            )

        return Order.objects.filter(
            user=user
        ).order_by("-created_at")

    @transaction.atomic
    def create(self, request, *args, **kwargs):

        delivery_address = request.data.get("delivery_address")

        if not delivery_address:

            return Response(
                {
                    "error": "Delivery address is required."
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        cart, created = Cart.objects.get_or_create(
            user=request.user
        )

        cart_items = CartItem.objects.filter(
            cart=cart
        )

        if not cart_items.exists():

            return Response(
                {
                    "error": "Your cart is empty."
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        total_amount = Decimal("0.00")

        order = Order.objects.create(
            user=request.user,
            delivery_address_id=delivery_address,
        )

        for cart_item in cart_items:

            price = (
                cart_item.menu_item.discount_price
                if cart_item.menu_item.discount_price
                else cart_item.menu_item.price
            )

            item_total = price * cart_item.quantity

            total_amount += item_total

            OrderItem.objects.create(
                order=order,
                menu_item=cart_item.menu_item,
                quantity=cart_item.quantity,
                price=price,
            )

        order.total_amount = total_amount
        order.save()

        cart_items.delete()

        return Response(
            OrderSerializer(order).data,
            status=status.HTTP_201_CREATED,
        )


class OrderDetailView(generics.RetrieveUpdateAPIView):

    serializer_class = OrderSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        user = self.request.user

        if user.is_staff:
            return Order.objects.all()

        if user.role == "restaurant_owner":

            return Order.objects.filter(
                items__menu_item__restaurant__owner=user
            ).distinct()

        return Order.objects.filter(
            user=user
        )


class CancelOrderView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request, pk):

        try:

            order = Order.objects.get(
                id=pk,
                user=request.user
            )

        except Order.DoesNotExist:

            return Response(
                {
                    "error": "Order not found."
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        if order.status != "pending":

            return Response(
                {
                    "error": "Only pending orders can be cancelled."
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        order.status = "cancelled"

        order.save()

        return Response(
            {
                "message": "Order cancelled successfully.",
                "order": OrderSerializer(order).data,
            }
        )


class OrderHistoryView(generics.ListAPIView):

    serializer_class = OrderSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        return Order.objects.filter(
            user=self.request.user
        ).order_by("-created_at")