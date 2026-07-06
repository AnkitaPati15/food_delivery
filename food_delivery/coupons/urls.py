from django.urls import path

from .views import (
    CouponListCreateView,
    CouponDetailView,
)

urlpatterns = [

    path(
        "",
        CouponListCreateView.as_view(),
        name="coupon-list-create"
    ),

    path(
        "<int:pk>/",
        CouponDetailView.as_view(),
        name="coupon-detail"
    ),

]