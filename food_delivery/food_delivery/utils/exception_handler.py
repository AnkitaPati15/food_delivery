from rest_framework.views import exception_handler as drf_exception_handler
from rest_framework.response import Response
from rest_framework import status
import logging

logger = logging.getLogger(__name__)


def custom_exception_handler(exc, context):
    """
    Custom exception handler for DRF that logs exceptions and
    returns a standardized error response.
    """
    response = drf_exception_handler(exc, context)

    if response is None:
        logger.error(f"Unhandled exception: {exc}", exc_info=True)
        return Response(
            {
                "detail": "An unexpected error occurred. Please try again later.",
                "code": "internal_error",
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    if response.status_code >= 500:
        logger.error(
            f"Server error: {exc} - Status: {response.status_code}",
            exc_info=True,
        )

    return response
