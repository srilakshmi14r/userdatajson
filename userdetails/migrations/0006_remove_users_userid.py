# Generated by Django 3.0.4 on 2020-04-03 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userdetails', '0005_auto_20200401_1750'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='userid',
        ),
    ]