from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import (
    RegisterView,
    UserProfileView,
    profile,
    edit_profile,
    change_password,
    UserLoginView,
    UserLogoutView,
)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [

    # ---------- Frontend ----------
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),

    path("profile/", profile, name="profile"),
    path("edit-profile/", edit_profile, name="edit-profile"),
    path("change-password/", change_password, name="change-password"),

    # ---------- API ----------
    path("api/login/", TokenObtainPairView.as_view(), name="api-login"),
    path("token/refresh/", TokenRefreshView.as_view()),
    path("register/", RegisterView.as_view()),
    path("api/profile/", UserProfileView.as_view()),
]

