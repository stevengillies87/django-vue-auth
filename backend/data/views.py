from django.shortcuts import render
from rest_framework import permissions, viewsets
from .models import AuthRequiredData, PermissionRequiredData, PublicData
from .permissions import DataPermission
from .serializers import (
    AuthRequiredDataSerializer,
    PermissionRequiredDataSerializer,
    PublicDataSerializer,
)


class AuthRequiredDataViewSet(viewsets.ModelViewSet):
    queryset = AuthRequiredData.objects.all()
    serializer_class = AuthRequiredDataSerializer
    permission_classes = [permissions.IsAuthenticated]


class PermissionRequiredDataViewSet(viewsets.ModelViewSet):
    queryset = PermissionRequiredData.objects.all()
    serializer_class = PermissionRequiredDataSerializer
    permission_classes = [DataPermission]


class PublicDataViewSet(viewsets.ModelViewSet):
    queryset = PublicData.objects.all()
    serializer_class = PublicDataSerializer
    permission_classes = [permissions.AllowAny]
