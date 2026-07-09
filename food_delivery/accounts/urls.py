from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import (
    RegisterView,
    UserProfileView,
    change_password,
    profile,
    edit_profile,
    change_password,
)


urlpatterns = [

    path('register/', RegisterView.as_view()),

    path('login/', TokenObtainPairView.as_view(), name='login'),

    path('token/refresh/', TokenRefreshView.as_view()),

    path('profile/', UserProfileView.as_view()),
    path(

    "profile/",

    profile,

    name="profile",

),
path(
    "edit-profile/",
    edit_profile,
    name="edit-profile",
),
path(
    "change-password/",
    change_password,
    name="change-password",
),
]