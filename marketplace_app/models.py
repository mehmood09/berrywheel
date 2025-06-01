from django.db import models

# Create your models here.
class ItemCategory(models.Model):
    name = models.CharField(max_length=250)
    date_added = models.DateField(auto_now_add=True)
    
    class Meta:
        ordering = ["-date_added"]
        verbose_name="ItemCategory"
        verbose_name_plural = "ItemCategories"
        
    def __str__(self):
        return self.name