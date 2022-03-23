from django.db import models


class Grade(models.Model):
    is_liked = models.BooleanField(
        default=True,
    )
    user = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
        related_name="grades",
        blank=True,
        null=True
    )