# Generated by Django 4.0.5 on 2022-06-20 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='model',
            name='old_price',
        ),
    ]
