from rest_framework import generics

from .models import Coupon
from .serializers import CouponSerializer


class CouponListCreateView(generics.ListCreateAPIView):

    queryset = Coupon.objects.filter(is_active=True)

    serializer_class = CouponSerializer


class CouponDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Coupon.objects.all()

    serializer_class = CouponSerializer