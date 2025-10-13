from django.urls import path, include
from django.contrib import admin
from . import views
from .views import *

urlpatterns = [
    
    #path('', views.home, name='home'),
    path('', RecipleListView.as_view(), name= 'recipe-list'),
    path('recipes/<int:pk>/', RecipeDetailView.as_view(), name= 'recipe-detail'),
    path('recipes/new/', RecipeCreateView.as_view(), name= 'recipe-create'),
    path('recipes/<int:pk>/delete', RecipeDeleteView.as_view(), name='recipe-delete'),
    path('recipes/<int:pk>/update', RecipeUpdateView.as_view(), name= 'recipe-update'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    path('signup/',views.signup, name='signup'), 
    path('myrecipe/',views.my_recipes, name='myrecipe'), 

]