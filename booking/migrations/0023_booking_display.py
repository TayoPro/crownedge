# Generated by Django 4.0.3 on 2022-05-13 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0022_remove_booking_display'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='display',
            field=models.BooleanField(default=True),
        ),
    ]
