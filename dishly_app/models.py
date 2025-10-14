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
    image_url = models.URLField(blank =True, max_length=500,  help_text="Paste a full recipe image https://URL")

    # Users who liked this recipe
    likes = models.ManyToManyField(User, related_name='liked_recipes', blank=True)


    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(
        max_length=2,
        choices=CATEGORIES,
        default=CATEGORIES[0][0]
    )
    ingredients = models.ManyToManyField(Ingredient, related_name="recipes")
    
    def total_likes(self):
        return self.likes.count()
    
    def __str__(self):
        return self.name

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("recipe-detail", kwargs={"recipe_id": self.id})

    class Meta:
        ordering = ['-created_at']



