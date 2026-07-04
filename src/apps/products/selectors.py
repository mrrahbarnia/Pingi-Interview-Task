from .models import Product


def product_exists_by_name(name: str) -> bool:
    return Product.objects.filter(name=name).exists()


def get_product_by_id(product_id: int) -> Product | None:
    return Product.objects.filter(id=product_id).first()
