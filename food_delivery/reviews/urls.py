from django.urls import path

from .views import (
    RestaurantReviewListCreateView,
    RestaurantReviewDetailView,
    MenuItemReviewListCreateView,
    MenuItemReviewDetailView,
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
]