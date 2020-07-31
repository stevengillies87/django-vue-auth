from .models import AuthRequiredData, PermissionRequiredData, PublicData
import random, string


class AuthRequiredDataFactory:
    @classmethod
    def create(cls):
        return AuthRequiredData.objects.create(data=get_random_string(20))


class PermissionRequiredDataFactory:
    @classmethod
    def create(cls):

        return PermissionRequiredData.objects.create(data=get_random_string(20))


class PublicDataFactory:
    @classmethod
    def create(cls):
        return PublicData.objects.create(data=get_random_string(20))


def get_random_string(length):
    return "".join(random.choice(string.ascii_lowercase) for i in range(length))
