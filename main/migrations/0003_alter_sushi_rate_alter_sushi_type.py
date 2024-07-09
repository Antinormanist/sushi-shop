# Generated by Django 4.2.13 on 2024-07-08 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_sushi_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sushi',
            name='rate',
            field=models.SmallIntegerField(choices=[('1', 1), ('2', 2), ('3', 3)]),
        ),
        migrations.AlterField(
            model_name='sushi',
            name='type',
            field=models.CharField(choices=[('set', 'set'), ('kit', 'kit'), ('one', 'one')], max_length=3),
        ),
    ]
