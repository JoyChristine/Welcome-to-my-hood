# Generated by Django 4.0.5 on 2022-06-18 09:36

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_remove_profile_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='neighbourhood',
            name='image',
            field=cloudinary.models.CloudinaryField(default='https://res.cloudinary.com/dz275mqsc/image/upload/v1654858776/default_nbsolf.png', max_length=255, verbose_name='image'),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=cloudinary.models.CloudinaryField(default='https://res.cloudinary.com/dz275mqsc/image/upload/v1654858776/default_nbsolf.png', max_length=255, verbose_name='image'),
        ),
    ]
