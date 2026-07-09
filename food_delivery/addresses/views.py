from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import (
    get_object_or_404,
    redirect,
    render,
)

from .forms import AddressForm
from .models import Address

@login_required
def address_list(request):

    addresses = Address.objects.filter(
        user=request.user
    )

    return render(
        request,
        "addresses/address_list.html",
        {
            "addresses": addresses,
        },
    )
@login_required
def add_address(request):

    if request.method == "POST":

        form = AddressForm(request.POST)

        if form.is_valid():

            address = form.save(commit=False)

            address.user = request.user

            if address.is_default:

                Address.objects.filter(
                    user=request.user
                ).update(
                    is_default=False
                )

            address.save()

            messages.success(
                request,
                "Address added successfully."
            )

            return redirect("address-list")

    else:

        form = AddressForm()

    return render(
        request,
        "addresses/address_form.html",
        {
            "form": form,
            "title": "Add Address",
        },
    )
@login_required
def edit_address(request, pk):

    address = get_object_or_404(
        Address,
        pk=pk,
        user=request.user,
    )

    if request.method == "POST":

        form = AddressForm(
            request.POST,
            instance=address,
        )

        if form.is_valid():

            updated = form.save(commit=False)

            if updated.is_default:

                Address.objects.filter(
                    user=request.user
                ).exclude(
                    pk=updated.pk
                ).update(
                    is_default=False
                )

            updated.save()

            messages.success(
                request,
                "Address updated successfully."
            )

            return redirect("address-list")

    else:

        form = AddressForm(
            instance=address
        )

    return render(
        request,
        "addresses/address_form.html",
        {
            "form": form,
            "title": "Edit Address",
        },
    )
@login_required
def delete_address(request, pk):

    address = get_object_or_404(
        Address,
        pk=pk,
        user=request.user,
    )

    if request.method == "POST":

        address.delete()

        messages.success(
            request,
            "Address deleted successfully."
        )

        return redirect("address-list")

    return render(
        request,
        "addresses/address_delete.html",
        {
            "address": address,
        },
    )