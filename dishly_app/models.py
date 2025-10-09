from django.db import models

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    ingeredients = models.TextField(max_length = 300)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name