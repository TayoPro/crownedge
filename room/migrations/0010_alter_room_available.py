# Generated by Django 4.0.3 on 2022-05-11 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0009_alter_category_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='available',
            field=models.BooleanField(default=True),
        ),
    ]
