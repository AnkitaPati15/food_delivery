from django.urls import path

from .views import (
    CreatePaymentView,
    PaymentDetailView,
)


urlpatterns = [

    path(
        'create/',
        CreatePaymentView.as_view()
    ),

    path(
        '<int:pk>/',
        PaymentDetailView.as_view()
    ),
]