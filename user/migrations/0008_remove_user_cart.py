# Generated by Django 4.2.13 on 2024-07-12 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_user_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='cart',
        ),
    ]
