# Generated by Django 3.1.5 on 2021-02-19 02:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0022_delete_watchlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='watchers',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
