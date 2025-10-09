from django.urls import path

from . import views
from .views import *

urlpatterns = [
    
    #path('', views.home, name='home'),
    path('', RecipleListView.as_view(), name= 'recipe-list'),
    path('recipes/<int:pk>/', RecipeDetailView.as_view(), name= 'recipe-detail'),
    path('recipes/new/', RecipeCreateView.as_view(), name= 'recipe-create'),
    path('recipes/<int:pk>/delete', RecipeDeleteView.as_view(), name='recipe-delete')
]