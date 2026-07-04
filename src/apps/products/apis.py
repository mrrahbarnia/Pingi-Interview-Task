from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema

from . import selectors
from . import services
from . import serializers
from . import exceptions


class ProductCreateAPIView(APIView):
    @swagger_auto_schema(
        request_body=serializers.ProductCreateRequest,
        responses={
            status.HTTP_201_CREATED: serializers.ProductCreateResponse,
            status.HTTP_409_CONFLICT: "Product already exists",
        },
    )
    def post(self, request: Request) -> Response:
        serializer = serializers.ProductCreateRequest(data=request.data)
        serializer.is_valid(raise_exception=True)

        if selectors.product_exists_by_name(name=serializer.validated_data["name"]):
            raise exceptions.ProductAlreadyExists()

        product = services.create_product(name=serializer.validated_data["name"])

        response = serializers.ProductCreateResponse(product)

        return Response(
            response.data,
            status=status.HTTP_201_CREATED,
        )
