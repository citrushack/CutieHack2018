# Generated by Django 2.1 on 2018-09-22 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landingapp', '0002_auto_20180921_0801'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='appStatus',
            field=models.CharField(default='Pending', max_length=30),
        ),
    ]