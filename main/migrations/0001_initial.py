# Generated by Django 4.2.13 on 2024-07-11 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sushi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('price', models.PositiveIntegerField()),
                ('description', models.TextField(max_length=999)),
                ('slug', models.SlugField(max_length=64)),
                ('type', models.CharField(choices=[('set', 'set'), ('kit', 'kit'), ('one', 'one')], max_length=3)),
                ('image', models.ImageField(upload_to='sushi/')),
                ('rate', models.SmallIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
            ],
            options={
                'verbose_name': 'Суши',
                'verbose_name_plural': 'Суши',
                'db_table': 'sushi',
            },
        ),
    ]
