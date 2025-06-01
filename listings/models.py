from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from marketplace_app.models import ItemCategory

# Create your models here.
class CarListing(models.Model):
    title = models.CharField(max_length=255)
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    speed = models.IntegerField()
    power = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='car_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    favorited_by = models.ManyToManyField(User, related_name="favorite_listings", null=True, blank=True)
    category = models.ForeignKey(ItemCategory,on_delete=models.CASCADE)
    seller = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, related_name="listings"
    )
    def get_absolute_url(self):
        return reverse("listings:car_detail", args=[str(self.id)])
    
    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"