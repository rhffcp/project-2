# Generated by Django 3.1.5 on 2021-02-23 06:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0045_auto_20210223_0556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='date_time',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
