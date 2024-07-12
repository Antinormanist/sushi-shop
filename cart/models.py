from django.db import models
from django.conf import settings

from main.models import Sushi
# Create your models here.
class Cart(models.Model):
    sushi = models.ForeignKey(to=Sushi, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    
    @staticmethod
    def get_total_price(user):
        total = 0
        for product in Cart.objects.filter(user=user):
            total += product.amount * product.sushi.price
        return total