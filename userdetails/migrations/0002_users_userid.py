# Generated by Django 3.0.4 on 2020-04-01 11:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('userdetails', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='userid',
            field=models.CharField(default='none', max_length=100),
        ),
    ]
