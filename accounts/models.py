from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ROLES = (
        (1, 'Admin'),
        (2, 'Manager'),
        (3, 'Customer')
    )

    role = models.IntegerField(choices=ROLES, null=True, blank=True)

    @property
    def get_role(self):
        return self.role.get_display_name()
