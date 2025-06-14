from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(null=True, blank=True)
    published_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
