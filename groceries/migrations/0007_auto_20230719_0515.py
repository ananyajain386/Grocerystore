# Generated by Django 2.0.2 on 2023-07-19 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groceries', '0006_remove_sections_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='sections',
            name='Img',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='products',
            name='Img',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]