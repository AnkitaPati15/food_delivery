from django.urls import path

from .views import (
    CategoryListCreateView,
    CategoryDetailView,
    MenuItemListCreateView,
    MenuItemDetailView,
     owner_category_list,
    owner_category_create,
    owner_category_edit,
    owner_category_delete,
)



urlpatterns = [

    path(
        'categories/',
        CategoryListCreateView.as_view()
    ),

    path(
        'categories/<int:pk>/',
        CategoryDetailView.as_view()
    ),

    path(
        'items/',
        MenuItemListCreateView.as_view()
    ),

    path(
        'items/<int:pk>/',
        MenuItemDetailView.as_view()
    ),
    path(
    "owner/categories/",
    owner_category_list,
    name="owner-category-list",
),

path(
    "owner/categories/create/",
    owner_category_create,
    name="owner-category-create",
),

path(
    "owner/categories/<int:pk>/edit/",
    owner_category_edit,
    name="owner-category-edit",
),

path(
    "owner/categories/<int:pk>/delete/",
    owner_category_delete,
    name="owner-category-delete",
),
]