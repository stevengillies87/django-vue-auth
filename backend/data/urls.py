from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    AuthRequiredDataViewSet,
    PermissionRequiredDataViewSet,
    PublicDataViewSet,
)

app_name = "data"

router = DefaultRouter()
router.register("auth-required", AuthRequiredDataViewSet, basename="auth-required")
router.register(
    "permission-required", PermissionRequiredDataViewSet, basename="permission-required"
)
router.register("public", PublicDataViewSet, basename="public")

urlpatterns = [
    path("", include(router.urls)),
]
