from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsRestaurantOwner(BasePermission):
    """
    Allows access only to restaurant owners.
    """

    message = "Only restaurant owners can perform this action."

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == "restaurant_owner"
        )


class IsCustomer(BasePermission):
    """
    Allows access only to customers.
    """

    message = "Only customers can perform this action."

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == "customer"
        )


class IsDeliveryPartner(BasePermission):
    """
    Allows access only to delivery partners.
    """

    message = "Only delivery partners can perform this action."

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == "delivery_partner"
        )


class IsAdmin(BasePermission):
    """
    Allows access only to Django admins.
    """

    message = "Admin access required."

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.is_staff
        )


class IsRestaurantOwnerOrAdmin(BasePermission):
    """
    Allows access to restaurant owners or admins.
    """

    message = "Only restaurant owners or admins can perform this action."

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and (
                request.user.role == "restaurant_owner"
                or request.user.is_staff
            )
        )


class IsOwnerOrReadOnly(BasePermission):

    message = "You do not have permission to modify this object."

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True

        if not request.user.is_authenticated:
            return False

        if request.user.is_staff:
            return True

        owner = getattr(obj, "owner", None)

        if owner:
            return owner == request.user

        user = getattr(obj, "user", None)

        if user:
            return user == request.user

        return False