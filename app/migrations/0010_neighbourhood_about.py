# Generated by Django 4.0.5 on 2022-06-19 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_neighbourhood_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='neighbourhood',
            name='about',
            field=models.TextField(blank=True),
        ),
    ]
