from django.urls import path
from .views import (
    CartView,
    AddToCartView,
    CartItemDetailView,
    IncreaseCartItemQuantityView,
    DecreaseCartItemQuantityView,
    
    cart_page,
    add_to_cart,

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
path(
    "",
    cart_page,
    name="cart-page",
),

path(
    "add/<int:menu_item_id>/",
    add_to_cart,
    name="add-to-cart",
),
]