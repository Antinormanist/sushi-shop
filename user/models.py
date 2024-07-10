from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    image = models.ImageField(upload_to='user_images/', blank=True, null=True, verbose_name='аватарка')
    phone = models.CharField(max_length=24, blank=True, null=True, verbose_name='телефон')
    address = models.CharField(max_length=255, blank=True, null=True, verbose_name='адрес')