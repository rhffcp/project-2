# Generated by Django 3.1.5 on 2021-02-23 05:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0043_listing_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 23, 5, 54, 17, 65736, tzinfo=utc)),
        ),
    ]
