# Generated by Django 4.2.7 on 2024-02-02 02:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0003_timeclock_time_worked'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TimeClock',
        ),
    ]
