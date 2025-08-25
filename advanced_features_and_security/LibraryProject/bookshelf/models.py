from django.contrib.auth.models import AbstractUser
from django.db import models

class Customer(AbstractUser):
    # You can add extra fields if needed, e.g. role, phone, etc.
    role = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.username

class Book(models.Model):
    """
    Example Book model with custom permissions.
    """
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()

    def _str_(self):
        return self.title

    class Meta:
        permissions = [
            ("can_view", "Can view book"),
            ("can_create", "Can create book"),
            ("can_edit", "Can edit book"),
            ("can_delete", "Can delete book"),
        ]

