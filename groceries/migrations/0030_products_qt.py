# Generated by Django 2.1 on 2023-09-09 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groceries', '0029_cart_ordered'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='qt',
            field=models.IntegerField(blank=True, default=1),
        ),
    ]
