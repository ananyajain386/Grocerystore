# Generated by Django 2.0 on 2023-07-18 09:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        ('groceries', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProductName', models.CharField(default='', max_length=30)),
                ('Mf_Date', models.DateField()),
                ('Ep_Date', models.DateField()),
                ('Priceperun', models.IntegerField(default=0)),
                ('Img', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='register',
            fields=[
                ('User', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('Userame', models.CharField(default='', max_length=30)),
                ('Firstname', models.CharField(default='', max_length=30)),
                ('Lastname', models.CharField(default='', max_length=30)),
                ('Email', models.EmailField(default='', error_messages={'unique': 'A user with that email already exists.'}, max_length=50, unique=True)),
                ('Password', models.CharField(default='', max_length=100)),
                ('Login', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='sections',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SectionName', models.CharField(default='', max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='login',
        ),
    ]
