from rest_framework import serializers


class ErrorResponse(serializers.Serializer):
    detail = serializers.CharField(
        help_text="A human-readable description of the error."
    )


class ProductCreateRequest(serializers.Serializer):
    name = serializers.CharField(max_length=255)


class ProductCreateResponse(serializers.Serializer):
    id = serializers.IntegerField()


class RegistrationCreateResponse(serializers.Serializer):
    uuid = serializers.UUIDField()
    created_at = serializers.DateTimeField()
