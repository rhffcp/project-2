# Generated by Django 3.1.5 on 2021-02-23 05:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0042_auto_20210222_0355'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='date_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]