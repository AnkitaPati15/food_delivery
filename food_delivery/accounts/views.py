from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import User
from .serializers import (
    RegisterSerializer,
    UserProfileSerializer
)
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def profile(request):

    context = {

        "user": request.user

    }

    return render(

        request,

        "accounts/profile.html",

        context

    )

class RegisterView(generics.CreateAPIView):

    queryset = User.objects.all()

    serializer_class = RegisterSerializer

    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        validated_data = serializer.validated_data

        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            role=validated_data['role'],
            phone_number=validated_data.get('phone_number')
        )

        user.set_password(validated_data['password'])

        user.save()

        return Response(
            RegisterSerializer(user).data,
            status=status.HTTP_201_CREATED
        )


class UserProfileView(generics.RetrieveAPIView):

    serializer_class = UserProfileSerializer

    permission_classes = [IsAuthenticated]

    def get_object(self):

        return self.request.user