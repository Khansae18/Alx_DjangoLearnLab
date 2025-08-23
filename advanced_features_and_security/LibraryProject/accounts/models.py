from django.contrib.auth.models import AbstractUser
from django.db import models


class Customer(AbstractUser):
    """
    Custom user model replacing Django's default User.
    """
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    def _str_(self):
        return self.username