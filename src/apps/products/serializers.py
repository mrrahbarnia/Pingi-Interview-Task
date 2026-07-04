from rest_framework import serializers


class ProductCreateRequest(serializers.Serializer):
    name = serializers.CharField(max_length=255)


class ProductCreateResponse(serializers.Serializer):
    id = serializers.IntegerField()
