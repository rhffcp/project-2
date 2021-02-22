# pylint: disable=no-member
# pylint: disable=unused-wildcard-import

from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django import forms

from .models import *

# add option for more than one photo and option for deleting upload.


class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'description', 'starting_bid', 'image', 'category']
        widgets = {'title': forms.TextInput(attrs={'class': "form-control", 'placeholder': "Title"}),
                   'description': forms.Textarea(attrs={'class': "form-control", 'style': "height: 300px", 'placeholder': "Description"}),
                   'starting_bid': forms.NumberInput(attrs={'class': "form-control", 'placeholder': "Starting Bid"}),
                   'category': forms.Select(attrs={'class': "form-control"})}


class BidForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = ['new_bid']
        widgets = {'new_bid': forms.NumberInput(
            attrs={'class': "form-control", 'placeholder': "Bid"})}


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
        widgets = {'comment': forms.Textarea(
            attrs={'class': "form-control", 'style': "height: 100px", 'placeholder': "Comment"})}


def index(request):
    return render(request, "auctions/index.html", {
        "listings": Listing.objects.all()
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def create(request):
    if request.method == "POST":

        # Get form and file data and place it inside form variable.
        form = ListingForm(request.POST, request.FILES)

        # If form is valid, save form data to model.
        if form.is_valid():
            creation = form.save()
            creation.creator = request.user
            creation.save()
            # go to listing page or creation success alert

    return render(request, "auctions/create.html", {
        "form": ListingForm()
    })


def listing(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    bid_error = False
    bid_placed = False
    user = request.user
    winner = listing.top_bidder
    access_error = False

    if listing.top_bidder is None:
        winner = "None"

    if request.user.is_authenticated:
        logged_in = True
    else:
        logged_in = False

    if request.user in listing.watchers.all():
        watcher_exists = True
    else:
        watcher_exists = False

    if request.method == "POST":
        if logged_in:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save()
                comment.listing = listing
                comment.user = request.user
                comment.save()

            form = BidForm(request.POST)
            if form.is_valid():
                bid_num = form.cleaned_data["new_bid"]
                if listing.current_bid is None:
                    if bid_num > listing.starting_bid:
                        listing.current_bid = bid_num
                        listing.top_bidder = request.user
                        listing.save()
                        new_bid = form.save()
                        new_bid.listing = listing
                        new_bid.user = request.user
                        new_bid.save()
                        bid_placed = True
                    else:
                        bid_error = True
                else:
                    if bid_num > listing.current_bid:
                        listing.current_bid = bid_num
                        listing.top_bidder = request.user
                        listing.save()
                        new_bid = form.save()
                        new_bid.listing = listing
                        new_bid.user = request.user
                        new_bid.save()
                        bid_placed = True
                    else:
                        bid_error = True
        else:
            access_error = True

    return render(request, "auctions/listing.html", {
        "listing": listing,
        "logged_in": logged_in,
        "watcher_exists": watcher_exists,
        "form": BidForm(),
        "bid_error": bid_error,
        "bid_placed": bid_placed,
        "user": user,
        "winner": winner,
        "comment_form": CommentForm(),
        "comments": listing.comments.all(),
        "access_error": access_error,
    })


def edit_watchlist(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    if request.user in listing.watchers.all():
        listing.watchers.remove(request.user)
    else:
        listing.watchers.add(request.user)
    return HttpResponseRedirect(reverse("listing", kwargs={'listing_id': listing_id}))


def winner(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    if listing.top_bidder is not None:
        listing.top_bidder = Bid.objects.filter(listing=listing).last().user
        listing.status = False
        listing.save()
    else:
        listing.status = False
        listing.save()
    return HttpResponseRedirect(reverse("listing", kwargs={'listing_id': listing_id}))


def watchlist(request):
    listings = request.user.watchlist.all()

    return render(request, "auctions/watchlist.html", {
        "listings": listings
    })
