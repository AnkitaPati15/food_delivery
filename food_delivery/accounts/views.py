from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render

from .forms import (
    ProfileUpdateForm,
    CustomPasswordChangeForm,
)


class UserLoginView(LoginView):

    template_name = "accounts/login.html"


class UserLogoutView(LogoutView):

    next_page = "/"


@login_required
def profile(request):

    return render(
        request,
        "accounts/profile.html",
        {
            "user": request.user,
        },
    )


@login_required
def edit_profile(request):

    if request.method == "POST":

        form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user,
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Profile updated successfully.",
            )

            return redirect("profile")

    else:

        form = ProfileUpdateForm(
            instance=request.user,
        )

    return render(
        request,
        "accounts/edit_profile.html",
        {
            "form": form,
        },
    )


@login_required
def change_password(request):

    if request.method == "POST":

        form = CustomPasswordChangeForm(
            request.user,
            request.POST,
        )

        if form.is_valid():

            user = form.save()

            update_session_auth_hash(
                request,
                user,
            )

            messages.success(
                request,
                "Password changed successfully.",
            )

            return redirect("profile")

    else:

        form = CustomPasswordChangeForm(
            request.user,
        )

    return render(
        request,
        "accounts/change_password.html",
        {
            "form": form,
        },
    )