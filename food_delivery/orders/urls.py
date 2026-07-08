from django.urls import path

from .views import (
    OrderListCreateView,
    OrderDetailView,
    CancelOrderView,
    OrderHistoryView,
    checkout,
    place_order,
    order_history,
)

urlpatterns = [

    path(
        "",
        OrderListCreateView.as_view(),
        name="order-list-create",
    ),

    path(
        "history/",
        OrderHistoryView.as_view(),
        name="order-history",
    ),

    path(
        "<int:pk>/",
        OrderDetailView.as_view(),
        name="order-detail",
    ),

    path(
        "<int:pk>/cancel/",
        CancelOrderView.as_view(),
        name="cancel-order",
    ),
    path(
    "checkout/",
    checkout,
    name="checkout",
),
path(
    "place/",
    place_order,
    name="place-order",
),
path(
    "history/",
    order_history,
    name="order-history",
),
]