from django.db import IntegrityError, transaction
from django.db.models import F

from . import selectors
from . import exceptions
from .models import Product, Registration
from .exceptions import ProductAlreadyExists


def create_product(name: str) -> Product:
    if selectors.product_exists_by_name(name):
        raise ProductAlreadyExists()

    try:
        return Product.objects.create(name=name)
    except IntegrityError:
        raise ProductAlreadyExists()


def update_product_capacity(product_id) -> int:
    return Product.objects.filter(
        id=product_id,
        registration_count__lt=F("capacity"),
    ).update(
        registration_count=F("registration_count") + 1,
    )


def create_registration(product_id: int) -> Registration:
    return Registration.objects.create(
        product_id=product_id,
    )


def register_product(product_id: int) -> Registration:
    with transaction.atomic():
        affected_rows = update_product_capacity(product_id)
        if affected_rows == 0:
            if not selectors.get_product_by_id(product_id):
                raise exceptions.ProductNotFound()

            raise exceptions.ProductCapacityExceeded()

        return create_registration(product_id)
