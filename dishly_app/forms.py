from django import forms
from .models import Recipe, Ingredient

class RecipeForm(forms.ModelForm):
    ingredients = forms.ModelMultipleChoiceField(
        queryset=Ingredient.objects.all().order_by('name'),
        widget=forms.CheckboxSelectMultiple(attrs={
            "id": "ingredient-list"
        })
    )

    class Meta:
        model = Recipe
        fields = ["name", "description", "category", "ingredients"]