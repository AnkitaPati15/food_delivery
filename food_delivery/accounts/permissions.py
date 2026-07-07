from rest_framework.permissions import BasePermission


class IsCustomer(BasePermission):
    """
    Permission to check if user has the customer role.
    """

    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.role == "customer"
        )


class IsRestaurantOwnerOrAdmin(BasePermission):
    """
    Permission to check if user is a restaurant owner or admin staff.
    """

    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and (
                request.user.is_staff
                or request.user.role == "restaurant_owner"
            )
        )
