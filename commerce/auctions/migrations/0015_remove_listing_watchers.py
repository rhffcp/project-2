# Generated by Django 3.1.5 on 2021-02-19 00:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0014_auto_20210219_0037'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='watchers',
        ),
    ]
