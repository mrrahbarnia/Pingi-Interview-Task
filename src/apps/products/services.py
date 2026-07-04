from django.db import IntegrityError

from .models import Product
from .exceptions import ProductAlreadyExists


def create_product(name: str) -> Product:

    try:
        return Product.objects.create(name=name)
    except IntegrityError:
        raise ProductAlreadyExists()
