from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)

    capacity = models.PositiveIntegerField(default=1_000_000)

    registration_count = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
