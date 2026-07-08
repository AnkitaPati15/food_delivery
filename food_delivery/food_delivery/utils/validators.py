from django.core.exceptions import ValidationError
import re


def validate_phone_number(value):
    """
    Validate phone number format (10-15 digits).
    """
    if not re.match(r"^\+?1?\d{9,15}$", value):
        raise ValidationError(
            "Phone number must be 10-15 digits, optionally starting with + or 1."
        )


def validate_positive_number(value):
    """
    Validate that a number is positive.
    """
    if value <= 0:
        raise ValidationError("This field must be a positive number.")


def validate_discount_percentage(value):
    """
    Validate discount percentage (0-100).
    """
    if not 0 <= value <= 100:
        raise ValidationError("Discount percentage must be between 0 and 100.")
