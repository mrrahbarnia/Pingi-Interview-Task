from rest_framework.response import Response
from rest_framework.views import exception_handler

from apps.products.exceptions import ApplicationException


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        return response

    if isinstance(exc, ApplicationException):
        return Response(
            {"detail": exc.detail},
            status=exc.status_code,
        )

    return None
