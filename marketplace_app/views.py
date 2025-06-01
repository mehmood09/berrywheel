from django.shortcuts import render,redirect, get_object_or_404, HttpResponse
from marketplace_app.forms import CategoryForm, CarListForm
from .models import ItemCategory
from listings.models import CarListing

# Create your views here.
def index(request):
    categories = ItemCategory.objects.all()
    context = {
        "categories" : categories
    }
    return render(request, "marketplace_app/index.html", context)

def listings(request, category_id):
    listings = CarListing.objects.filter(category=category_id)
    category = ItemCategory.objects.get(pk=category_id)
    
    context = {"listings" : listings,"category" : category }
    return render(request, "marketplace_app/listings.html", context)


def add_category(request):
    if request.method == "POST":
        #print(request)
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("marketplace_app:index")
        else:
            return render(request, "marketplace_app/add_category.html", context)
    else:
        form = CategoryForm()
        context = {"form": form}
        return render(request, "marketplace_app/add_category.html", context)

def add_car(request, category_id=None):
    category = None
    initial_data = {}
    if category_id:
        category = get_object_or_404(ItemCategory, id = category_id)
        initial_data = {"category": category}
        
    if request.method == "POST":
        form = CarListForm(request.POST,request.FILES, initial=initial_data)
        if form.is_valid():
            new_car = form.save(commit=False)
            new_car.user = request.user
            new_car = form.save() # ("recipes:index")
            return redirect("marketplace_app:listings", category_id = new_car.category.id)
    else:
        form = CarListForm(initial=initial_data)
    
    context = {"form" : form,"category": category} #recipes
    return render(request,"marketplace_app/add_car.html",context)      

