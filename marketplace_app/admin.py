from django.contrib import admin
from .models import ItemCategory

class ItemCategoryAdmin(admin.ModelAdmin):
    list_display = ("id","name","date_added")
    search_fields = ["name"]

# Register your models here.
admin.site.register(ItemCategory, ItemCategoryAdmin)