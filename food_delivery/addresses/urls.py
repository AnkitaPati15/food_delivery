from django.urls import path

from .views import (
    address_list,
    add_address,
    edit_address,
    delete_address,
)

urlpatterns = [

    path(
        "",
        address_list,
        name="address-list",
    ),

    path(
        "add/",
        add_address,
        name="add-address",
    ),

    path(
        "edit/<int:pk>/",
        edit_address,
        name="edit-address",
    ),

    path(
        "delete/<int:pk>/",
        delete_address,
        name="delete-address",
    ),
]