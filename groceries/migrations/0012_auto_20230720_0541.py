# Generated by Django 2.0.2 on 2023-07-20 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groceries', '0011_auto_20230719_0640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sections',
            name='SectionName',
            field=models.CharField(default='', max_length=30, unique=True),
        ),
    ]
