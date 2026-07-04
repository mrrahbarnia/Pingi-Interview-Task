from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from . import services
from . import serializers


class ProductCreateAPIView(APIView):
    @swagger_auto_schema(
        request_body=serializers.ProductCreateRequest,
        responses={
            status.HTTP_201_CREATED: serializers.ProductCreateResponse,
            status.HTTP_409_CONFLICT: openapi.Response(
                description="Product already exists.",
                schema=serializers.ErrorResponse,
            ),
        },
    )
    def post(self, request: Request) -> Response:
        serializer = serializers.ProductCreateRequest(data=request.data)
        serializer.is_valid(raise_exception=True)

        product = services.create_product(name=serializer.validated_data["name"])

        response = serializers.ProductCreateResponse(product)

        return Response(
            response.data,
            status=status.HTTP_201_CREATED,
        )


class RegistrationCreateAPIView(APIView):
    @swagger_auto_schema(
        operation_summary="Register for a product",
        operation_description=(
            "Registers a client for the specified product and returns "
            "a unique UUID. If the product has reached its maximum "
            "capacity, the request is rejected."
        ),
        request_body=None,
        responses={
            status.HTTP_201_CREATED: serializers.RegistrationCreateResponse,
            status.HTTP_404_NOT_FOUND: openapi.Response(
                description="Product not found.",
                schema=serializers.ErrorResponse,
            ),
            status.HTTP_400_BAD_REQUEST: openapi.Response(
                description="Product capacity is full.",
                schema=serializers.ErrorResponse,
            ),
        },
    )
    def post(self, request: Request, product_id: int) -> Response:
        registration = services.register_product(product_id)

        response = serializers.RegistrationCreateResponse(registration)

        return Response(
            response.data,
            status=status.HTTP_201_CREATED,
        )
