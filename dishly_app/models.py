from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


CATEGORIES = (
   ('AR', 'Arabic'),
   ('IT', 'Italian'),
   ('AS', 'Asian'),
   ('AM', 'American'),
   ('DS', 'Dessert'),
   ('IC', 'Ice Cream'),
   ('VG', 'Vegan'),
   ('SF', 'Seafood'),
)


class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name



class Recipe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)


    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(
        max_length=2,
        choices=CATEGORIES,
        default=CATEGORIES[0][0]
    )
    ingredients = models.ManyToManyField(Ingredient, related_name="recipes")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("recipe-detail", kwargs={"recipe_id": self.id})

    class Meta:
        ordering = ['-created_at']



