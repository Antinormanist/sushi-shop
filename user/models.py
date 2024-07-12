from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth import get_user_model
from django.conf import settings

from cart.models import Cart
# Create your models here.
    
class Profile(models.Model):
    user = models.OneToOneField(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    last_name = models.CharField(max_length=128, blank=True, null=True, default='anonymous')
    first_name = models.CharField(max_length=128, blank=True, null=True, default='anonymous')
    patronymic = models.CharField(max_length=128, blank=True, null=True, default='anonymous')
    phone = models.CharField(max_length=24, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return f'{self.user} profile'


class User(AbstractUser):
    image = models.ImageField(upload_to='user_images/', blank=True, null=True, verbose_name='аватарка')