# Generated by Django 4.0.3 on 2022-05-12 21:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0021_booking_display'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='display',
        ),
    ]
