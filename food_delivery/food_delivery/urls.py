"""
URL configuration for food_delivery project.
"""

from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(

    openapi.Info(
        title="Food Delivery API",
        default_version="v1",
        description="Food Delivery Backend APIs",
        contact=openapi.Contact(
            email="admin@example.com"
        ),
    ),

    public=True,

    permission_classes=[permissions.AllowAny],

)


urlpatterns = [

    # ----------------------------
    # Admin
    # ----------------------------

    path(
        "admin/",
        admin.site.urls,
    ),

    # ----------------------------
    # Frontend Authentication
    # ----------------------------

    path(
        "accounts/",
        include("accounts.urls"),
    ),

    # ----------------------------
    # API Authentication
    # ----------------------------

    path(
        "api/accounts/",
        include("accounts.urls"),
    ),

    # ----------------------------
    # Menu APIs
    # ----------------------------

    path(
        "api/menu/",
        include("menu.urls"),
    ),

    # ----------------------------
    # Cart APIs
    # ----------------------------

    path(
        "api/cart/",
        include("cart.urls"),
    ),

    # ----------------------------
    # Order APIs
    # ----------------------------

    path(
        "api/orders/",
        include("orders.urls"),
    ),

    # ----------------------------
    # Payment APIs
    # ----------------------------

    path(
        "api/payments/",
        include("payments.urls"),
    ),

    # ----------------------------
    # Review APIs
    # ----------------------------

    path(
        "api/reviews/",
        include("reviews.urls"),
    ),

    # ----------------------------
    # Coupon APIs
    # ----------------------------

    path(
        "api/coupons/",
        include("coupons.urls"),
    ),

    # ----------------------------
    # Addresses
    # ----------------------------

    path(
        "addresses/",
        include("addresses.urls"),
    ),

    # ----------------------------
    # Restaurants & Frontend Pages
    # ----------------------------

    path(
        "",
        include("restaurants.urls"),
    ),

    # ----------------------------
    # DRF Login
    # ----------------------------

    path(
        "api-auth/",
        include("rest_framework.urls"),
    ),

    # ----------------------------
    # Swagger
    # ----------------------------

    path(
        "swagger/",
        schema_view.with_ui(
            "swagger",
            cache_timeout=0,
        ),
        name="schema-swagger-ui",
    ),

    path(
        "redoc/",
        schema_view.with_ui(
            "redoc",
            cache_timeout=0,
        ),
        name="schema-redoc",
    ),
]


urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT,
)