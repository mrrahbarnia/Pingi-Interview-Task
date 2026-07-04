import uuid

from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)

    capacity = models.PositiveIntegerField(default=1_000_000)

    registration_count = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)


class Registration(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="registrations",
    )

    created_at = models.DateTimeField(auto_now_add=True)
