# Generated by Django 4.2.13 on 2024-07-12 07:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sushi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.sushi')),
            ],
        ),
    ]
