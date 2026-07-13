from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from menu.models import MenuItem

from .models import Cart, CartItem
from .serializers import CartItemSerializer, CartSerializer


@login_required
def cart_page(request):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    items = CartItem.objects.filter(cart=cart).select_related("menu_item")

    context = {
        "cart": cart,
        "items": items,
        "total": cart.total_price,
    }

    return render(request, "cart/cart.html", context)


@login_required
def add_to_cart(request, menu_item_id):
    menu_item = get_object_or_404(MenuItem, pk=menu_item_id)
    cart, _ = Cart.objects.get_or_create(user=request.user)

    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        menu_item=menu_item,
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    messages.success(request, "Item added to cart.")
    return redirect(request.META.get("HTTP_REFERER", "cart-page"))


@login_required
@require_POST
def increase_cart_item(request, pk):
    cart_item = get_object_or_404(CartItem, pk=pk, cart__user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    messages.success(request, "Quantity updated.")
    return redirect("cart-page")


@login_required
@require_POST
def decrease_cart_item(request, pk):
    cart_item = get_object_or_404(CartItem, pk=pk, cart__user=request.user)

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
        messages.success(request, "Quantity updated.")
    else:
        cart_item.delete()
        messages.success(request, "Item removed from cart.")

    return redirect("cart-page")


@login_required
@require_POST
def remove_cart_item(request, pk):
    cart_item = get_object_or_404(CartItem, pk=pk, cart__user=request.user)
    cart_item.delete()
    messages.success(request, "Item removed from cart.")
    return redirect("cart-page")


class CartView(generics.RetrieveAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        cart, _ = Cart.objects.get_or_create(user=self.request.user)
        return cart


class AddToCartView(generics.CreateAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        menu_item_id = request.data.get("menu_item")
        quantity = int(request.data.get("quantity", 1))

        menu_item = MenuItem.objects.get(id=menu_item_id)

        if not menu_item.is_available:
            return Response(
                {"error": "This item is currently unavailable."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if not menu_item.restaurant.is_active:
            return Response(
                {"error": "Restaurant is currently unavailable."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        cart, _ = Cart.objects.get_or_create(user=request.user)

        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            menu_item=menu_item,
            defaults={"quantity": quantity},
        )

        if not created:
            cart_item.quantity += quantity
            cart_item.save()

        return Response(
            CartItemSerializer(cart_item).data,
            status=status.HTTP_201_CREATED,
        )


class CartItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]


class IncreaseCartItemQuantityView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        try:
            cart_item = CartItem.objects.get(id=pk, cart__user=request.user)
        except CartItem.DoesNotExist:
            return Response(
                {"error": "Cart item not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        cart_item.quantity += 1
        cart_item.save()

        return Response(CartItemSerializer(cart_item).data, status=status.HTTP_200_OK)


class DecreaseCartItemQuantityView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        try:
            cart_item = CartItem.objects.get(id=pk, cart__user=request.user)
        except CartItem.DoesNotExist:
            return Response(
                {"error": "Cart item not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
            return Response({"message": "Item removed from cart."}, status=status.HTTP_200_OK)

        return Response(CartItemSerializer(cart_item).data, status=status.HTTP_200_OK)
    