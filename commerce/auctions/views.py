# pylint: disable=no-member
# pylint: disable=unused-wildcard-import

from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django import forms

from .models import *


class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'description', 'starting_bid', 'image', 'category']
        widgets = {'title': forms.TextInput(attrs={'class': "form-control", 'placeholder': "Title"}),
                   'description': forms.Textarea(attrs={'class': "form-control", 'style': "height: 300px", 'placeholder': "Description"}),
                   'starting_bid': forms.NumberInput(attrs={'class': "form-control", 'placeholder': "Starting Bid"}),
                   'category': forms.Select(attrs={'class': "form-control"})}


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
            form.save()
            # go to listing page

    return render(request, "auctions/create.html", {
        "form": ListingForm()
    })


def listing(request, listing_id):
    listing = Listing.objects.get(id=listing_id)

    if request.user.is_authenticated:
        logged_in = True
    else:
        logged_in = False

    if request.user in listing.watchers.all():
        exist = True
        added = True
    else:
        exist = False
        added = False

    return render(request, "auctions/listing.html", {
        "listing": listing,
        "logged_in": logged_in,
        "exist": exist,
        "added": added
    })


def edit_watchlist(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    if request.user in listing.watchers.all():
        listing.watchers.remove(request.user)
    else:
        listing.watchers.add(request.user)
    return HttpResponseRedirect(reverse("listing", kwargs={'listing_id': listing_id}))

    