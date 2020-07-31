from rest_framework import serializers

from .models import AuthRequiredData, PermissionRequiredData, PublicData


class AuthRequiredDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthRequiredData
        fields = "__all__"


class PermissionRequiredDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PermissionRequiredData
        fields = "__all__"


class PublicDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicData
        fields = "__all__"
