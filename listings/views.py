from datetime import datetime
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from marketplace_app.forms import CarListForm
from .models import CarListing
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.
def listings(request):
    listings = CarListing.objects.all()
    #print("recipes", recipes)
    context = {"listings": listings}
    return render(request,"listings/listings.html", context)


def car_detail(request, car_id):
    #recipe = Recipe.objects.get(id=recipe_id)
    car = get_object_or_404(CarListing, id=car_id)
    context = {"car":car}
    return render(request,"listings/listing.html",context)

@login_required
def toggle_favorite(request, car_id):
    car = get_object_or_404(CarListing, id=car_id)

    if request.user in car.favorited_by.all():
        car.favorited_by.remove(request.user)
    else:
        car.favorited_by.add(request.user)
    return redirect("listings:car_detail", car_id=car_id)

@login_required
def favorite_listings(request):
    user = request.user
    favorites = user.favorite_listings.all()
    context = {"listings": favorites}
    return render(request, "listings/favorite_listings.html", context)
