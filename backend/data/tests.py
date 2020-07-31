from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from rest_framework import status, test
from accounts.factories import UserFactory
from .factories import (
    AuthRequiredDataFactory,
    PermissionRequiredDataFactory,
    PublicDataFactory,
)
from .models import PermissionRequiredData


class AuthRequiredDataAPITestCase(test.APITestCase):
    def setUp(self):
        UserFactory.create_user(username="user1", password="pwd321")
        for n in range(1, 10):
            AuthRequiredDataFactory.create()

    def test_request_data__no_auth__forbidden_response(self):
        response = self.client.get(reverse("data:auth-required-list"))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_request_data__auth__ok_response(self):
        self.assertTrue(self.client.login(username="user1", password="pwd321"))
        response = self.client.get(reverse("data:auth-required-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class PermissionRequiredDataAPITestCase(test.APITestCase):
    def setUp(self):
        self.user = UserFactory.create_user(username="user1", password="pwd321")
        for n in range(1, 10):
            PermissionRequiredDataFactory.create()

    def test_request_data__no_permission__forbidden_response(self):
        self.assertTrue(self.client.login(username="user1", password="pwd321"))
        response = self.client.get(reverse("data:permission-required-list"))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_request_data__auth__ok_response(self):
        content_type = ContentType.objects.get_for_model(PermissionRequiredData)
        permission = Permission.objects.get(
            content_type=content_type, codename=f"view_{PermissionRequiredData._meta.model_name}",
        )
        self.user.user_permissions.add(permission)
        self.assertTrue(self.client.login(username="user1", password="pwd321"))
        response = self.client.get(reverse("data:permission-required-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class PublicDataAPITestCase(test.APITestCase):
    def setUp(self):
        UserFactory.create_user(username="user1", password="pwd321")
        for n in range(1, 10):
            PublicDataFactory.create()

    def test_request_data__no_auth__ok_response(self):
        response = self.client.get(reverse("data:public-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_request_data__auth__ok_response(self):
        self.assertTrue(self.client.login(username="user1", password="pwd321"))
        response = self.client.get(reverse("data:public-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
