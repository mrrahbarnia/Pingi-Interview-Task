from .models import Product


def product_exists_by_name(name: str) -> bool:
    return Product.objects.filter(name=name).exists()
