from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Recipe
from .forms import RecipeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required



class Home(LoginView):
    template_name = ''


def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

class RecipleListView(ListView):
    model = Recipe
    template_name = 'dishly_app/home.html'
    context_object_name = 'object_list'

def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    query = self.request.GET.get('search')

    if query and query.strip():  # ✅ Only run search if text exists
        context['all_search_results'] = Recipe.objects.filter(name__icontains=query)
    else:
        context['all_search_results'] = None  # ✅ Nothing will show in template

    return context


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'dishly_app/recipes/details.html'
    context_object_name = 'recipe'

class RecipeCreateView(LoginRequiredMixin,CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'dishly_app/recipes/recipe_create.html'
    success_url = reverse_lazy("recipe-list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def handle_no_permission(self):
        return redirect('/')
        
class RecipeUpdateView(LoginRequiredMixin,UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'dishly_app/recipes/recipe_create.html'
    success_url = reverse_lazy("recipe-list")
    context_object_name = 'recipe'
    def handle_no_permission(self):
        return redirect('/')

class RecipeDeleteView(LoginRequiredMixin,DeleteView):
    model = Recipe
    template_name = 'dishly_app/recipes/recipe_confirm_delete.html'
    success_url = reverse_lazy("recipe-list")
    

    context_object_name = 'recipe'
    def handle_no_permission(self):
        return redirect('/')
    
    
    
    

    

@login_required(login_url=reverse_lazy('recipe-list'), redirect_field_name=None)
def my_recipes(request):
    recipes = Recipe.objects.filter(user=request.user)
    return render(request, 'dishly_app/myrecipe.html', {'recipes': recipes})


# Auth

def signup(request):
    error_message = ''
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/")
    else:
        error_message = 'Invalid sign up - try again!'
    form = UserCreationForm()
        
    return render(request, "registration/signup.html", {'form': form, 'error_message': error_message})
