from django.urls import path

from .views import (
    UserLoginView,
    UserLogoutView,
    profile,
    edit_profile,
    change_password,
)

urlpatterns = [

    path(
        "login/",
        UserLoginView.as_view(),
        name="login",
    ),

    path(
        "logout/",
        UserLogoutView.as_view(),
        name="logout",
    ),

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