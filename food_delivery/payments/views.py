from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Payment
from .serializers import PaymentSerializer

from orders.models import Order


class CreatePaymentView(generics.CreateAPIView):

    serializer_class = PaymentSerializer

    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):

        order_id = request.data.get('order')

        payment_method = request.data.get(
            'payment_method'
        )

        order = Order.objects.get(
            id=order_id
        )

        payment = Payment.objects.create(
            order=order,
            payment_method=payment_method,
            amount=order.total_amount,
            payment_status='pending'
        )

        return Response(
            PaymentSerializer(payment).data,
            status=status.HTTP_201_CREATED
        )


class PaymentDetailView(
    generics.RetrieveUpdateAPIView
):

    queryset = Payment.objects.all()

    serializer_class = PaymentSerializer

    permission_classes = [IsAuthenticated]