# Generated by Django 3.1.5 on 2021-02-24 00:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0048_remove_listing_date_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='date_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
