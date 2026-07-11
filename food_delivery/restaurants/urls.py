from django.urls import path

from .views import (
    home,
    owner_dashboard,
    owner_restaurant_delete,
    restaurant_detail,
    RestaurantListCreateView,
    RestaurantDetailView,
    owner_restaurant_list,
    owner_restaurant_create,
    owner_restaurant_edit,
    owner_analytics
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
    name="restaurant-detail",
),
path(
    "owner/dashboard/",
    owner_dashboard,
    name="owner-dashboard",
),
path(
    "owner/restaurants/",
    owner_restaurant_list,
    name="owner-restaurant-list",
),
path(
    "owner/restaurants/create/",
    owner_restaurant_create,
    name="restaurant-create",
),
path(
    "owner/restaurants/<int:pk>/edit/",
    owner_restaurant_edit,
    name="restaurant-edit",
),
path(
    "owner/restaurants/<int:pk>/delete/",
    owner_restaurant_delete,
    name="restaurant-delete",
),
path(
    "owner/analytics/",
    owner_analytics,
    name="owner-analytics",
),
]