import random

from .models import User


class UserFactory:
    @staticmethod
    def create_user(username=None, password=None, **kwargs):
        return User.objects.create_user(username=username, password=password, **kwargs)

