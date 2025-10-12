from django.shortcuts import render ,redirect
from django.views.generic import ListView, DetailView, CreateView,UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Recipe
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

# def home(request):
#     return render(request, "dishly_app/home.html")

class Home(LoginView):
  template_name = ''

def about(request):
  return render(request, 'about.html')

def contact(request):
  return render(request, 'contact.html')

class RecipleListView(ListView):
    model = Recipe
    template_name = 'dishly_app/home.html'
    

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'dishly_app/recipes/details.html'
    context_object_name = 'recipe'
    
    
class RecipeCreateView(CreateView):
    model = Recipe
    fields = '__all__'
    template_name = 'dishly_app/recipes/recipe_create.html'
    success_url = reverse_lazy("recipe-list")
    
    def form_valid(self, form):
        form.instance.user = self.request.user
    # Now let's have the CreateView class do its normal job and take over
        return super().form_valid(form)
    


class RecipeUpdateView(UpdateView):
    model = Recipe
    fields = '__all__'
    template_name = 'dishly_app/recipes/recipe_create.html'
    success_url = reverse_lazy("recipe-list") 
    context_object_name = 'recipe'
    
    
    
class RecipeDeleteView(DeleteView):
    model = Recipe
    template_name = 'dishly_app/recipes/recipe_confirm_delete.html'
    success_url = reverse_lazy("recipe-list") 
    context_object_name = 'recipe'


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()          
            login(request, user)        
            return redirect("/")    
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})