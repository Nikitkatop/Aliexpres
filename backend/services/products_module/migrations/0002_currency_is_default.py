# Generated by Django 4.1.1 on 2023-02-18 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products_module', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='currency',
            name='is_default',
            field=models.BooleanField(default=False, verbose_name='Default'),
        ),
    ]