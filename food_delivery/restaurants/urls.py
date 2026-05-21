from django.urls import path

from .views import (
    RestaurantListCreateView,
    RestaurantDetailView,
)


urlpatterns = [

    path(
        '',
        RestaurantListCreateView.as_view()
    ),

    path(
        '<int:pk>/',
        RestaurantDetailView.as_view()
    ),
]