# Generated by Django 5.0.6 on 2024-09-20 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_alquiler', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videojuego',
            name='stock',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
