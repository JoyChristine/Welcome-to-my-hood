# Generated by Django 4.0.5 on 2022-06-18 09:22

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_remove_neighbourhood_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=cloudinary.models.CloudinaryField(blank=True, default='https://res.cloudinary.com/dz275mqsc/image/upload/v1654858776/default_nbsolf.png', max_length=255, null=True, verbose_name='image'),
        ),
    ]
