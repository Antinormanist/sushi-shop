# Generated by Django 4.2.13 on 2024-07-09 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_sushi_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sushi',
            name='rate',
            field=models.SmallIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]),
        ),
    ]
