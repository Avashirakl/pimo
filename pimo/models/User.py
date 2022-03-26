from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser, models.Model):
    username = models.CharField(
        max_length=20,
        unique=True,
        blank=True,
        null=True,
    )
    first_name = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )
    last_name = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )
    email = models.EmailField(
        unique=True,
        blank=True,
        null=True
    )

    @property
    def likes(self):
        return self.grades.filter(is_liked=True).count()

    @property
    def dislikes(self):
        return self.grades.filter(is_liked=False).count()

    def __str__(self):
        return self.username
