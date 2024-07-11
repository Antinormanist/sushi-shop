# Generated by Django 4.2.13 on 2024-07-11 20:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.AddField(
            model_name='user',
            name='profile',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.profile'),
        ),
    ]
