# Generated by Django 2.1 on 2023-09-07 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groceries', '0022_products_section'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sections',
            name='removed',
            field=models.BooleanField(default=False),
        ),
    ]