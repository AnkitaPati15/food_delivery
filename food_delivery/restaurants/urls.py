from django.urls import path

from .views import (
    home,
    owner_dashboard,
    restaurant_detail,
    RestaurantListCreateView,
    RestaurantDetailView,
)

urlpatterns = [

    # Homepage
    path(
        "",
        home,
        name="home",
    ),

    # Restaurant APIs
    path(
        "api/",
        RestaurantListCreateView.as_view(),
        name="restaurant-list",
    ),

    path(
        "api/<int:pk>/",
        RestaurantDetailView.as_view(),
        name="restaurant-detail",
    ),
    path(
    "restaurants/<int:pk>/",
    restaurant_detail,
    name="restaurant-detail-page",
),
path(
    "owner/dashboard/",
    owner_dashboard,
    name="owner-dashboard",
),
]