# Generated by Django 4.0.3 on 2022-05-11 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0010_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='booking_code',
            field=models.CharField(default='a', max_length=50),
        ),
    ]
