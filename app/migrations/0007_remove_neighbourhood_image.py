# Generated by Django 4.0.5 on 2022-06-18 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_neighbourhood_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='neighbourhood',
            name='image',
        ),
    ]
