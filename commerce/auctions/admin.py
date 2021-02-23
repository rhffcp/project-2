# pylint: disable=unused-wildcard-import

from django.contrib import admin

from .models import *

class CommentAdmin(admin.ModelAdmin):
    list_display = ("user", "listing", "comment")

class BidAdmin(admin.ModelAdmin):
    list_display = ("user", "listing", "new_bid")

# Register your models here.
admin.site.register(User)
admin.site.register(Listing)
admin.site.register(Bid, BidAdmin)
admin.site.register(Comment, CommentAdmin)