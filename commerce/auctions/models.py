from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

# Model for each item listing.
class Listing(models.Model):
    categories = [
        ('FASH', 'Fashion'),
        ('CHILD', 'Children'),
        ('ELEC', 'Electronics'),
        ('HOME', 'Home'),
        ('SER', 'Services'),
        ('BOOK', 'Books'),
        ('ART', 'Music/Arts'),
        ('OTHER', 'Other')
    ]

    creation_date = models.DateTimeField()
    title = models.CharField(max_length=64)
    photo = models.URLField()
    description = models.CharField(max_length=200)
    starting_bid = models.FloatField()
    current_bid = models.FloatField()
    category = models.CharField(choices=categories, max_length=5)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField()
    
class Bid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    new_bid = models.FloatField()

class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    date = models.DateTimeField()