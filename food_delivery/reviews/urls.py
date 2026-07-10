from django.urls import path

from .views import (
    RestaurantReviewListCreateView,
    RestaurantReviewDetailView,
    MenuItemReviewListCreateView,
    MenuItemReviewDetailView,
   owner_restaurant_reviews,
   owner_menu_reviews,
 

)


urlpatterns = [

    path(
        'restaurants/',
        RestaurantReviewListCreateView.as_view()
    ),

    path(
        'restaurants/<int:pk>/',
        RestaurantReviewDetailView.as_view()
    ),

    path(
        'menu-items/',
        MenuItemReviewListCreateView.as_view()
    ),

    path(
        'menu-items/<int:pk>/',
        MenuItemReviewDetailView.as_view()
    ),
    path(
    "owner/reviews/restaurants/",
    owner_restaurant_reviews,
    name="owner-restaurant-reviews",
),

path(
    "owner/reviews/menu/",
    owner_menu_reviews,
    name="owner-menu-reviews",
),
]