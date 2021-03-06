# Generated by Django 2.0.6 on 2018-10-05 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landingapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='date_of_birth',
        ),
        migrations.AddField(
            model_name='profile',
            name='Gender',
            field=models.CharField(blank=True, choices=[('Female', 'Female'), ('Male', 'Male'), ('Other', 'Other'), ('Prefer not to disclose', 'Prefer not to disclose')], max_length=30),
        ),
        migrations.AddField(
            model_name='profile',
            name='LevelofStudy',
            field=models.CharField(choices=[('1st Year', '1st Year'), ('2nd Year', '2nd Year'), ('3rd Year', '3rd Year'), ('4th Year', '4th Year'), ('5th Year or beyond', '5th Year or beyond'), ('Prefer not to disclose', 'Prefer not to disclose')], default='', max_length=30),
        ),
        migrations.AddField(
            model_name='profile',
            name='Race',
            field=models.CharField(blank=True, choices=[('Asian', 'Asian'), ('Black or African American', 'Black or African American'), ('Latino or Latin American', 'Latino or Latin American'), ('Native American', 'Native American'), ('Native Hawaiian or other Pacific Islander', 'Native Hawaiian or other Pacific Islander'), ('Other', 'Other'), ('Prefer not to diclose', 'Prefer not to disclose'), ('Two or more races', 'Two or more races'), ('White', 'White')], max_length=30),
        ),
        migrations.AddField(
            model_name='profile',
            name='Resume',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='age',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='appStatus',
            field=models.CharField(default='Pending', max_length=30),
        ),
        migrations.AddField(
            model_name='profile',
            name='conductBox',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='dietRestrictions',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='gradYear',
            field=models.CharField(choices=[('2019', '2019'), ('2020', '2020'), ('2021', '2021'), ('2022', '2022'), ('2023', '2023'), ('2024', '2024'), ('2025', '2025')], default='', max_length=30),
        ),
        migrations.AddField(
            model_name='profile',
            name='meme',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='profile',
            name='phoneNumber',
            field=models.CharField(blank=True, max_length=12),
        ),
        migrations.AddField(
            model_name='profile',
            name='shareBox',
            field=models.BooleanField(default=False),
        ),
    ]
