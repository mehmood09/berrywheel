from django.urls import path
from . import views
from listings import views

app_name = "listings"
urlpatterns = [
    path("", views.listings, name="index"),
    path("<int:car_id>", views.car_detail, name="car_detail"),
    path("<int:car_id>/toggle_favorite",views.toggle_favorite, name="toggle_favorite"),
    path("my-favorites/",views.favorite_listings, name="favorite_listings"),
    # path("<int:car_id>/delete/",views.delete_car, name="delete_car"),
    # path("<int:car_id>/edit/",views.edit_car, name="edit_car"),
]
