"""
Application-wide constants.
"""

# User Roles
ROLE_CUSTOMER = "customer"
ROLE_RESTAURANT_OWNER = "restaurant_owner"
ROLE_DELIVERY_PARTNER = "delivery_partner"

ROLE_CHOICES = [
    (ROLE_CUSTOMER, "Customer"),
    (ROLE_RESTAURANT_OWNER, "Restaurant Owner"),
    (ROLE_DELIVERY_PARTNER, "Delivery Partner"),
]

# Order Statuses
ORDER_STATUS_PENDING = "pending"
ORDER_STATUS_CONFIRMED = "confirmed"
ORDER_STATUS_PREPARING = "preparing"
ORDER_STATUS_READY = "ready"
ORDER_STATUS_OUT_FOR_DELIVERY = "out_for_delivery"
ORDER_STATUS_DELIVERED = "delivered"
ORDER_STATUS_CANCELLED = "cancelled"

ORDER_STATUS_CHOICES = [
    (ORDER_STATUS_PENDING, "Pending"),
    (ORDER_STATUS_CONFIRMED, "Confirmed"),
    (ORDER_STATUS_PREPARING, "Preparing"),
    (ORDER_STATUS_READY, "Ready"),
    (ORDER_STATUS_OUT_FOR_DELIVERY, "Out for Delivery"),
    (ORDER_STATUS_DELIVERED, "Delivered"),
    (ORDER_STATUS_CANCELLED, "Cancelled"),
]

# Payment Statuses
PAYMENT_STATUS_PENDING = "pending"
PAYMENT_STATUS_COMPLETED = "completed"
PAYMENT_STATUS_FAILED = "failed"
PAYMENT_STATUS_REFUNDED = "refunded"

PAYMENT_STATUS_CHOICES = [
    (PAYMENT_STATUS_PENDING, "Pending"),
    (PAYMENT_STATUS_COMPLETED, "Completed"),
    (PAYMENT_STATUS_FAILED, "Failed"),
    (PAYMENT_STATUS_REFUNDED, "Refunded"),
]

# Pagination
DEFAULT_PAGE_SIZE = 10
MAX_PAGE_SIZE = 100

# Cache timeout in seconds
CACHE_TIMEOUT_SHORT = 60  # 1 minute
CACHE_TIMEOUT_MEDIUM = 300  # 5 minutes
CACHE_TIMEOUT_LONG = 3600  # 1 hour
