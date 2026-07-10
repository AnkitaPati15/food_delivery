from django.shortcuts import render

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import filters, generics
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)

from .models import Restaurant
from .serializers import RestaurantSerializer
from django.shortcuts import get_object_or_404
from menu.models import Category
from menu.models import Category, MenuItem
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from menu.models import MenuItem
from orders.models import Order


@login_required
def owner_dashboard(request):

    restaurants = Restaurant.objects.filter(
        owner=request.user
    )

    menu_items = MenuItem.objects.filter(
        restaurant__owner=request.user
    )

    orders = Order.objects.filter(
        items__menu_item__restaurant__owner=request.user
    ).distinct()

    revenue = sum(
        order.total_amount
        for order in orders
    )

    context = {

        "restaurant_count": restaurants.count(),

        "menu_count": menu_items.count(),

        "order_count": orders.count(),

        "revenue": revenue,

    }

    return render(
        request,
        "owner/dashboard.html",
        context,
    )


def restaurant_detail(request, pk):

    restaurant = get_object_or_404(
        Restaurant,
        pk=pk
    )

    categories = Category.objects.filter(
        restaurant=restaurant
    )

    menu_items = MenuItem.objects.filter(
        restaurant=restaurant,
        is_available=True
    )

    context = {
        "restaurant": restaurant,
        "categories": categories,
        "menu_items": menu_items,
    }

    return render(
        request,
        "restaurants/restaurant_detail.html",
        context,
    )

def home(request):

    restaurants = Restaurant.objects.active()[:6]

    context = {
        "restaurants": restaurants
    }

    return render(
        request,
        "home.html",
        context
    )


class RestaurantListCreateView(generics.ListCreateAPIView):

    serializer_class = RestaurantSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    filterset_fields = [
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
        "delivery_time",
        "minimum_order",
        "delivery_fee",
        "average_rating",
    ]

    ordering = [
        "name",
    ]

    def get_permissions(self):

        if self.request.method == "POST":
            return [IsAuthenticated()]

        return [IsAuthenticatedOrReadOnly()]

    def get_queryset(self):

        return Restaurant.objects.active()

    def perform_create(self, serializer):

        if self.request.user.role != "restaurant_owner":
            raise PermissionError(
                "Only restaurant owners can create restaurants."
            )

        serializer.save(owner=self.request.user)


class RestaurantDetailView(
    generics.RetrieveUpdateDestroyAPIView
):

    serializer_class = RestaurantSerializer

    permission_classes = [
        IsAuthenticatedOrReadOnly
    ]

    def get_queryset(self):

        if self.request.method in [
            "PUT",
            "PATCH",
            "DELETE",
        ]:

            if not self.request.user.is_authenticated:
                return Restaurant.objects.none()

            if self.request.user.is_superuser:
                return Restaurant.objects.active()

            return Restaurant.objects.filter(
                owner=self.request.user
            )

        return Restaurant.objects.active()