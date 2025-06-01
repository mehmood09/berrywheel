from django.contrib import admin
from .models import CarListing

class CarListingAdmin(admin.ModelAdmin):
    list_display = ("id","title","brand","model","year","speed","power","price","description","created_at","category","seller")
    search_fields = ["title"]

# Register your models here.
admin.site.register(CarListing,CarListingAdmin)