from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

# Model for each item listing.
class Listing(models.Model):
    categories = [
        ('a', 'Books'),
        ('b', 'Clothing'),
        ('c', 'Children'),
        ('d', 'Electronics'),
        ('e', 'Furniture'),
        ('f', 'Kitchen'),
        ('g', 'Music/Arts'),
        ('h', 'Services'),
        ('i', 'Tools'),
        ('j', 'Other')
    ]

    # creation_date = models.DateTimeField(null=True)
    title = models.CharField(max_length=100)
    image = models.URLField("Image URL (optional)", null=True, blank=True)
    description = models.CharField(max_length=300)
    starting_bid = models.FloatField("Starting Bid")
    # current_bid = models.FloatField()
    category = models.CharField("Category (optional)", choices=categories, default=categories[9], max_length=1, null=True, blank=True)
    # buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    # status = models.BooleanField()

    def __str__(self):
        return f"{self.title}"
    
class Bid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    new_bid = models.FloatField()

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=300)
    date = models.DateTimeField()