from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(
        verbose_name="Email",
        unique=True,
    )  # email of User
    phone = models.CharField(
        max_length=35,
        verbose_name="Mobile phone number",
        blank=True,
        null=True,
    )  # mobile phone number of User
    city = models.CharField(
        max_length=55,
        verbose_name="City",
        blank=True,
        null=True,
    )  # city of User

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
