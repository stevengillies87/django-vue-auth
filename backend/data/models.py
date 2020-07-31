from django.db import models


class PublicData(models.Model):
    data = models.CharField(max_length=60)


class AuthRequiredData(models.Model):
    data = models.CharField(max_length=60)


class PermissionRequiredData(models.Model):
    data = models.CharField(max_length=60)
