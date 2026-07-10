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
from django.contrib import messages
from django.shortcuts import render, redirect
from cart.models import Cart, CartItem
from decimal import Decimal
from django.contrib import messages
from django.shortcuts import redirect
from django.db import transaction

from cart.models import Cart, CartItem
from addresses.models import Address
from .models import Order, OrderItem
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
)

from .forms import OrderStatusForm


def checkout(request):

    cart, created = Cart.objects.get_or_create(
        user=request.user
    )

    items = CartItem.objects.filter(
        cart=cart
    )

    if not items.exists():

        messages.warning(
            request,
            "Your cart is empty."
        )

        return redirect("cart-page")

    subtotal = Decimal("0.00")

    for item in items:

        price = (
            item.menu_item.discount_price
            if item.menu_item.discount_price
            else item.menu_item.price
        )

        subtotal += price * item.quantity

    delivery_fee = Decimal("50")

    total = subtotal + delivery_fee

    context = {

        "items": items,

        "subtotal": subtotal,

        "delivery_fee": delivery_fee,

        "total": total,

    }

    return render(
        request,
        "orders/checkout.html",
        context,
    )
@transaction.atomic
def place_order(request):

    if request.method != "POST":
        return redirect("checkout")

    cart, created = Cart.objects.get_or_create(
        user=request.user
    )

    cart_items = CartItem.objects.filter(
        cart=cart
    )

    if not cart_items.exists():

        messages.error(
            request,
            "Your cart is empty."
        )

        return redirect("cart-page")

    address = Address.objects.filter(
        user=request.user
    ).first()

    if not address:

        messages.error(
            request,
            "Please add an address first."
        )

        return redirect("checkout")

    order = Order.objects.create(

        user=request.user,

        delivery_address=address,

        status="pending"

    )

    total = 0

    for item in cart_items:

        price = (
            item.menu_item.discount_price
            if item.menu_item.discount_price
            else item.menu_item.price
        )

        OrderItem.objects.create(

            order=order,

            menu_item=item.menu_item,

            quantity=item.quantity,

            price=price,

        )

        total += price * item.quantity

    order.total_amount = total

    order.save()

    cart_items.delete()

    messages.success(
        request,
        "Order placed successfully."
    )

    return redirect(
        "order-history"
    )
def order_history(request):

    orders = Order.objects.filter(

        user=request.user

    ).order_by("-created_at")

    return render(

        request,

        "orders/order_history.html",

        {

            "orders": orders

        }

    )

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
    
@login_required
def owner_order_list(request):

    if request.user.role != "restaurant_owner":

        return redirect("/")

    orders = Order.objects.filter(
        items__menu_item__restaurant__owner=request.user
    ).distinct().order_by("-created_at")

    status = request.GET.get("status")

    if status:

        orders = orders.filter(status=status)

    return render(
        request,
        "owner/order_list.html",
        {
            "orders": orders,
            "selected_status": status,
            "status_choices": Order.STATUS_CHOICES,
        },
    )
@login_required
def owner_order_detail(request, pk):

    order = get_object_or_404(
        Order,
        pk=pk,
        items__menu_item__restaurant__owner=request.user,
    )

    return render(
        request,
        "owner/order_detail.html",
        {
            "order": order,
        },
    )
@login_required
def owner_order_status(request, pk):

    order = get_object_or_404(
        Order,
        pk=pk,
        items__menu_item__restaurant__owner=request.user,
    )

    if request.method == "POST":

        form = OrderStatusForm(
            request.POST,
            instance=order,
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Order status updated."
            )

            return redirect(
                "owner-order-detail",
                pk=order.id,
            )

    else:

        form = OrderStatusForm(
            instance=order,
        )

    return render(
        request,
        "owner/order_status.html",
        {
            "form": form,
            "order": order,
        },
    )    

