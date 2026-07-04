from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import permissions

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="Pingi API",
        default_version="v1",
        description="Interview Task API",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path("admin/", admin.site.urls),
    re_path(
        r"^docs/swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="swagger",
    ),
    path("products/", include("apps.products.urls")),
]
