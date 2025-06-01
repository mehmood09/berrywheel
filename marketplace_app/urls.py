from django.urls import path
from . import views

app_name = "marketplace_app"
urlpatterns = [
    path("",views.index, name="index"),
    # path("recipes/<int:category_id>/", views.recipes, name="recipes"),
    path("listings/<int:category_id>/", views.listings, name="listings"),
    path("add-category/", views.add_category, name="add_category"),
    path("add_car/", views.add_car, name="add_car_no_genre"),
    # path("add_car/category/<int:category_id>/", views.add_car, name="add_recipe_with_genre"),
   
]
