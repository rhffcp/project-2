# Generated by Django 3.1.5 on 2021-02-21 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0039_auto_20210221_0333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('a', 'Books'), ('b', 'Children'), ('c', 'Clothing'), ('d', 'Decoration'), ('e', 'Electronics'), ('f', 'Furniture'), ('g', 'Kitchen'), ('h', 'Music/Arts'), ('i', 'Services'), ('j', 'Tools'), ('k', 'Vehicles'), ('l', 'Other')], max_length=1, null=True),
        ),
    ]
