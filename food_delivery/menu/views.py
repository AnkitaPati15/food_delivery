from rest_framework import generics, status
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from rest_framework.response import Response

from accounts.permissions import (
    IsRestaurantOwnerOrAdmin,
)

from restaurants.models import Restaurant

from .models import (
    Category,
    MenuItem,
)

from .serializers import (
    CategorySerializer,
    MenuItemSerializer,
)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
)

from restaurants.models import Restaurant

from .forms import CategoryForm
from .models import Category


@login_required
def owner_category_list(request):

    categories = Category.objects.filter(
        restaurant__owner=request.user
    )

    return render(
        request,
        "owner/category_list.html",
        {
            "categories": categories,
        },
    )
@login_required
def owner_category_create(request):

    if request.user.role != "restaurant_owner":

        return redirect("/")

    if request.method == "POST":

        form = CategoryForm(request.POST)

        form.fields[
            "restaurant"
        ].queryset = Restaurant.objects.filter(
            owner=request.user
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Category created successfully."
            )

            return redirect(
                "owner-category-list"
            )

    else:

        form = CategoryForm()

        form.fields[
            "restaurant"
        ].queryset = Restaurant.objects.filter(
            owner=request.user
        )

    return render(
        request,
        "owner/category_form.html",
        {
            "form": form,
            "title": "Add Category",
        },
    )
@login_required
def owner_category_edit(request, pk):

    category = get_object_or_404(
        Category,
        pk=pk,
        restaurant__owner=request.user,
    )

    if request.method == "POST":

        form = CategoryForm(
            request.POST,
            instance=category,
        )

        form.fields[
            "restaurant"
        ].queryset = Restaurant.objects.filter(
            owner=request.user
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Category updated successfully."
            )

            return redirect(
                "owner-category-list"
            )

    else:

        form = CategoryForm(
            instance=category,
        )

        form.fields[
            "restaurant"
        ].queryset = Restaurant.objects.filter(
            owner=request.user
        )

    return render(
        request,
        "owner/category_form.html",
        {
            "form": form,
            "title": "Edit Category",
        },
    )
@login_required
def owner_category_delete(request, pk):

    category = get_object_or_404(
        Category,
        pk=pk,
        restaurant__owner=request.user,
    )

    if request.method == "POST":

        category.delete()

        messages.success(
            request,
            "Category deleted successfully."
        )

        return redirect(
            "owner-category-list"
        )

    return render(
        request,
        "owner/category_delete.html",
        {
            "category": category,
        },
    )


class CategoryListCreateView(generics.ListCreateAPIView):

    serializer_class = CategorySerializer

    queryset = Category.objects.all()

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_permissions(self):

        if self.request.method == "POST":
            return [
                IsAuthenticated(),
                IsRestaurantOwnerOrAdmin(),
            ]

        return [
            IsAuthenticatedOrReadOnly(),
        ]

    def perform_create(self, serializer):

        restaurant = serializer.validated_data["restaurant"]

        if (
            not self.request.user.is_staff
            and restaurant.owner != self.request.user
        ):
            raise PermissionError(
                "You can only add categories to your own restaurant."
            )

        serializer.save()


class CategoryDetailView(
    generics.RetrieveUpdateDestroyAPIView
):

    serializer_class = CategorySerializer

    permission_classes = [
        IsAuthenticatedOrReadOnly
    ]

    def get_queryset(self):

        if self.request.user.is_authenticated:

            if self.request.user.is_staff:
                return Category.objects.all()

            return Category.objects.filter(
                restaurant__owner=self.request.user
            )

        return Category.objects.all()


class MenuItemListCreateView(generics.ListCreateAPIView):

    serializer_class = MenuItemSerializer

    queryset = MenuItem.objects.all()

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_permissions(self):

        if self.request.method == "POST":
            return [
                IsAuthenticated(),
                IsRestaurantOwnerOrAdmin(),
            ]

        return [
            IsAuthenticatedOrReadOnly(),
        ]

    def perform_create(self, serializer):

        restaurant = serializer.validated_data["restaurant"]

        if (
            not self.request.user.is_staff
            and restaurant.owner != self.request.user
        ):
            raise PermissionError(
                "You can only add menu items to your own restaurant."
            )

        serializer.save()


class MenuItemDetailView(
    generics.RetrieveUpdateDestroyAPIView
):

    serializer_class = MenuItemSerializer

    permission_classes = [
        IsAuthenticatedOrReadOnly
    ]

    def get_queryset(self):

        if self.request.user.is_authenticated:

            if self.request.user.is_staff:
                return MenuItem.objects.all()

            return MenuItem.objects.filter(
                restaurant__owner=self.request.user
            )

        return MenuItem.objects.filter(
            is_available=True
        )