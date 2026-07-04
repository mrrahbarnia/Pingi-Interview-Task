from rest_framework import status
from rest_framework.test import APITestCase

from apps.products.models import Product, Registration


class ProductTests(APITestCase):
    def test_create_product(self):
        response = self.client.post(
            "/products/",
            {"name": "Laptop"},
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )

        self.assertEqual(
            Product.objects.count(),
            1,
        )

    def test_duplicate_name_returns_conflict(self):
        Product.objects.create(name="Laptop")

        response = self.client.post(
            "/products/",
            {"name": "Laptop"},
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_409_CONFLICT,
        )

        self.assertEqual(
            Product.objects.count(),
            1,
        )

    def test_successful_registration(self):
        product = Product.objects.create(
            name="Laptop",
            capacity=2,
        )

        response = self.client.post(
            f"/products/{product.id}/registrations/",  # type: ignore
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )

        self.assertEqual(
            Registration.objects.count(),
            1,
        )

        product.refresh_from_db()

        self.assertEqual(
            product.registration_count,
            1,
        )

    def test_product_not_found(self):
        response = self.client.post(
            "/products/9999/registrations/",
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_404_NOT_FOUND,
        )

    def test_capacity_exceeded(self):
        product = Product.objects.create(
            name="Laptop",
            capacity=1,
            registration_count=1,
        )

        response = self.client.post(
            f"/products/{product.id}/registrations/",  # type: ignore
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST,
        )

        self.assertEqual(
            Registration.objects.count(),
            0,
        )
