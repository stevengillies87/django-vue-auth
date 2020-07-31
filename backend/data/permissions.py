from rest_framework import permissions


class DataPermission(permissions.DjangoModelPermissions):
    def __init__(self):
        self.perms_map["GET"] = ["%(app_label)s.view_%(model_name)s"]
