# Generated by Django 2.1 on 2023-09-07 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groceries', '0024_auto_20230907_1329'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='Quantity',
        ),
    ]
