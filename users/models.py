from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone_number = models.CharField(max_length=13, unique=True)

    USERNAME_FIELD = "phone_number"

    def __str__(self):
        return self.username

    def is_this_admin(self):
        return self.is_superuser


class Customer(User):
    address = models.TextField()

    def __str__(self):
        return self.phone_number

