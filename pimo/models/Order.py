from django.db import models
from django.contrib.auth.models import AbstractUser
from pimo.models import User

STATUS_CHOICES = [
    ('ON', 'Opened'),
    ('INP', 'In progress'),
    ('DEL', 'Delayed'),
    ('OFF', 'Closed'),
    ('CND', 'Canceled'),
]


class Order(models.Model):
    title = models.CharField('Title', max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField('Publication date')
    deadline = models.DateTimeField('Deadline')
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default='ON')
    details = models.TextField('Details')

    def __str__(self):
        return self.title