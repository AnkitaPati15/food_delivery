from django.urls import path

from .views import (
    OrderListCreateView,
    OrderDetailView,
    CancelOrderView,
    OrderHistoryView,
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
]