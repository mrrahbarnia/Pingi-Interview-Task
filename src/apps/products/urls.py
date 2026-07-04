from django.urls import path

from . import apis

urlpatterns = [
    path(
        "",
        apis.ProductCreateAPIView.as_view(),
        name="product-create",
    ),
]
