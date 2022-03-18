from django.db import models
from pimo.models import Order

class Offer(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    cost = models.IntegerField('Cost')