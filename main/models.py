from django.db import models

RATE_CHOICES = [
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
]

TYPE_CHOICES = [
    ('set', 'set'),
    ('kit', 'kit'),
    ('one', 'one'),            
]

# Create your models here.
class Sushi(models.Model):
    name = models.CharField(max_length=32)
    price = models.PositiveIntegerField()
    description = models.TextField(max_length=999)
    slug = models.SlugField(max_length=64)
    type = models.CharField(max_length=3, choices=TYPE_CHOICES)
    image = models.ImageField(upload_to='sushi/')
    rate = models.SmallIntegerField(choices=RATE_CHOICES)
    
    class Meta:
        db_table = 'sushi'
        verbose_name = 'Суши'
        verbose_name_plural = 'Суши'
        
        
    def __str__(self):
        return self.name