from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

# Model for each item listing.
class Listing(models.Model):
    categories = [
        ('BOOK', 'Books'),
        ('CLOTH', 'Clothing'),
        ('CHILD', 'Children'),
        ('ELEC', 'Electronics'),
        ('FURN', 'Furniture'),
        ('KIT', 'Kitchen'),
        ('ART', 'Music/Arts'),
        ('SER', 'Services'),
        ('TOOL', 'Tools'),
        ('OTHER', 'Other')
    ]

    creation_date = models.DateTimeField()
    title = models.CharField(max_length=100)
    image = models.URLField("Image URL (optional)", null=True, blank=True)
    description = models.CharField(max_length=300)
    starting_bid = models.FloatField("Starting Bid")
    current_bid = models.FloatField()
    category = models.CharField("Category (optional)", choices=categories, max_length=5, null=True, blank=True)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField()
    
class Bid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    new_bid = models.FloatField()

class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=300)
    date = models.DateTimeField()