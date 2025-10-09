from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView,UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Recipe

# Create your views here.

def home(request):
    return render(request, "dishly_app/home.html")

class RecipleListView(ListView):
    model = Recipe
    template_name = 'recipe_list.html'