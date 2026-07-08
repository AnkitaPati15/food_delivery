from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """
    Permission to check if user is the owner of an object.
    Assumes the object has a 'user' field.
    """

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class IsRestaurantOwner(BasePermission):
    """
    Permission to check if user is the owner of a restaurant.
    """

    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.role == "restaurant_owner"
        )


class IsDeliveryPartner(BasePermission):
    """
    Permission to check if user is a delivery partner.
    """

    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.role == "delivery_partner"
        )


class IsAdminOrReadOnly(BasePermission):
    """
    Permission to allow only admins to write, anyone can read.
    """

    def has_permission(self, request, view):
        if request.method in ["GET", "HEAD", "OPTIONS"]:
            return True
        return request.user and request.user.is_staff
