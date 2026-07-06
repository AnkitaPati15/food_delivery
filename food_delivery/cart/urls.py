from django.urls import path
from .views import (
    CartView,
    AddToCartView,
    CartItemDetailView,
    IncreaseCartItemQuantityView,
    DecreaseCartItemQuantityView,
)


urlpatterns = [

    path(
        '',
        CartView.as_view()
    ),

    path(
        'add/',
        AddToCartView.as_view()
    ),

    path(
        'items/<int:pk>/',
        CartItemDetailView.as_view()
    ),
    path(
    "items/<int:pk>/increase/",
    IncreaseCartItemQuantityView.as_view(),
    name="increase-cart-item",
),

path(
    "items/<int:pk>/decrease/",
    DecreaseCartItemQuantityView.as_view(),
    name="decrease-cart-item",
),
]