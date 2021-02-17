from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

# Model for each item listing.
class Listing(models.Model):
    categories = [
        ('a', 'All Categories'),
        ('b', 'Books'),
        ('c', 'Clothing'),
        ('d', 'Children'),
        ('e', 'Electronics'),
        ('f', 'Furniture'),
        ('g', 'Kitchen'),
        ('h', 'Music/Arts'),
        ('i', 'Services'),
        ('j', 'Tools'),
        ('k', 'Other')
    ]

    # creation_date = models.DateTimeField(null=True)
    title = models.CharField(max_length=100)
    # Images are uploaded to 'media/images/' directory path within project.
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    description = models.CharField(max_length=300)
    starting_bid = models.FloatField()
    # current_bid = models.FloatField()
    category = models.CharField(choices=categories, default=categories[0], max_length=1, null=True, blank=True)
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