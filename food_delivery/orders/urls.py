from django.urls import path

from .views import (
    OrderListCreateView,
    OrderDetailView,
    CancelOrderView,
    OrderHistoryView,
    checkout,
    place_order,
    order_history,
    
    owner_order_list,
    owner_order_detail,
    owner_order_status,

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
path(
    "owner/orders/",
    owner_order_list,
    name="owner-order-list",
),

path(
    "owner/orders/<int:pk>/",
    owner_order_detail,
    name="owner-order-detail",
),

path(
    "owner/orders/<int:pk>/status/",
    owner_order_status,
    name="owner-order-status",
),
]