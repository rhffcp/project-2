from django.contrib.auth.models import AbstractUser
from django.db import models

CATEGORIES = [
    ('a', 'Books'),
    ('b', 'Children'),
    ('c', 'Clothing'),
    ('d', 'Decoration'),
    ('e', 'Electronics'),
    ('f', 'Furniture'),
    ('g', 'Kitchen'),
    ('h', 'Music/Arts'),
    ('i', 'Office'),
    ('j', 'Services'),
    ('k', 'Tools'),
    ('l', 'Vehicles'),
    ('m', 'Other')
]

class User(AbstractUser):
    pass

# Model for each item listing.
class Listing(models.Model):
    # creation_date = models.DateTimeField(null=True)
    title = models.CharField(max_length=100)
    # Images are uploaded to 'media/images/' directory path within project.
    image = models.ImageField(upload_to="images/", null=True)
    description = models.CharField(max_length=300)
    starting_bid = models.FloatField()
    current_bid = models.FloatField(blank=True, null=True)
    category = models.CharField(choices=CATEGORIES, max_length=1, null=True)
    top_bidder = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bidder", blank=True, null=True)
    status = models.BooleanField(default=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="creator", blank=True, null=True)
    watchers = models.ManyToManyField(User, blank=True, related_name="watchlist")

    def __str__(self):
        return f"{self.title}"
    
class Bid(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    new_bid = models.FloatField()

    

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    comment = models.CharField(max_length=300)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, blank=True, null=True, related_name="comments")
    # date = models.DateTimeField()
