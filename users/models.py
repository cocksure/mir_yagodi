from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=13)
    is_active = models.BooleanField(default=True)


class Basket(models.Model):
    berry = models.ForeignKey("berries.Berries", on_delete=models.CASCADE)

    def __str__(self):
        return self.berry

