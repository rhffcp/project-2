from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create, name="create"),
    path("listing/<int:listing_id>", views.listing, name="listing"),
    path("<int:listing_id>", views.edit_watchlist, name="edit_watchlist"),
    path("winner/<int:listing_id>", views.winner, name="winner"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("categories", views.categories, name="categories"),
    path("category_listings/<str:category>", views.category_listings, name="category_listings")
]
