# Generated by Django 5.0.6 on 2024-09-20 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_alquiler', '0002_alter_videojuego_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videojuego',
            name='stock',
            field=models.PositiveIntegerField(),
        ),
    ]
