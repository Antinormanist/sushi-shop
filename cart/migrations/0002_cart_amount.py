# Generated by Django 4.2.13 on 2024-07-12 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='amount',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
