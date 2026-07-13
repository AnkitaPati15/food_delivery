from django.urls import path

from .views import (
    AddToCartView,
    CartItemDetailView,
    CartView,
    DecreaseCartItemQuantityView,
    IncreaseCartItemQuantityView,
)

urlpatterns = [
    path("", CartView.as_view(), name="cart-api"),
    path("add/", AddToCartView.as_view(), name="add-to-cart-api"),
    path("items/<int:pk>/", CartItemDetailView.as_view(), name="cart-item-detail"),
    path(
        "items/<int:pk>/increase/",
        IncreaseCartItemQuantityView.as_view(),
        name="increase-cart-item-api",
    ),
    path(
        "items/<int:pk>/decrease/",
        DecreaseCartItemQuantityView.as_view(),
        name="decrease-cart-item-api",
    ),
]