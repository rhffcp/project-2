from django.contrib.auth.models import AbstractUser
from django.db import models

CATEGORIES = [
    ('a', 'Beauty'),
    ('b', 'Books'),
    ('c', 'Children'),
    ('d', 'Clothing'),
    ('e', 'Decoration'),
    ('f', 'Electronics'),
    ('g', 'Furniture'),
    ('h', 'Kitchen'),
    ('i', 'Music/Arts'),
    ('j', 'Office'),
    ('k', 'Services'),
    ('l', 'Tools'),
    ('m', 'Vehicles'),
    ('n', 'Other')
]


class User(AbstractUser):
    pass


class Listing(models.Model):
    title = models.CharField(max_length=100)
    # Images are uploaded to 'media/images/' directory within project. Requires settings and urls.
    image = models.ImageField(upload_to="images/", null=True)
    description = models.CharField(max_length=300)
    starting_bid = models.FloatField()
    current_bid = models.FloatField(blank=True, null=True)
    category = models.CharField(choices=CATEGORIES, max_length=1, null=True)
    top_bidder = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listings_by_bidder", blank=True, null=True)
    status = models.BooleanField(default=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listings_by_creator", blank=True, null=True)
    watchers = models.ManyToManyField(User, related_name="listings_by_watcher", blank=True)

    def __str__(self):
        return f"{self.title}"


class Bid(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    new_bid = models.FloatField()


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    comment = models.CharField(max_length=300)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="comments", blank=True, null=True)

    def __str__(self):
        return f"{self.comment}"
