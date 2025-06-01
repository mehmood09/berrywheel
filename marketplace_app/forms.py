from django import forms
from marketplace_app.models import ItemCategory
from listings.models import CarListing

class CategoryForm(forms.ModelForm):
    class Meta:
        model = ItemCategory
        fields = ["name"]
        #labels={"name":"Category Name"}
        widgets = {
            'name' : forms.TextInput(
                attrs={"placeholder":"Car Category Name", "size": "50"}
            )
        }

class CarListForm(forms.ModelForm):
    class Meta:
        model = CarListing
        fields= ["id","title","brand","model","year","speed","power","price","description","category","seller","image"]
        widgets = {
            'title' : forms.TextInput(attrs={"class" : "form-control","placeholder":"Car Title"}),
            'brand' : forms.TextInput(attrs={"class" : "form-control","placeholder":"Brand",}),
            'model' : forms.TextInput(attrs={"class" : "form-control","placeholder":"Model"}),
            'year' : forms.TextInput(attrs={"class" : "form-control","placeholder":"Year"}),
            'speed' : forms.TextInput(attrs={"class" : "form-control","placeholder":"Speed"}),
            'power' : forms.TextInput(attrs={"class" : "form-control","placeholder":"Power"}),
            'price' : forms.TextInput(attrs={"class" : "form-control","placeholder":"Price"}),
            'description' : forms.Textarea(attrs={"class" : "form-control","placeholder":"Description","row" : "2"}),
            'category' : forms.Select(attrs={"class" : "form-select"}),
            'seller' : forms.Select(attrs={"class" : "form-select"})
        }