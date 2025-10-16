from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Recipe
from .forms import RecipeForm



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
        query = self.request.GET.get('search', '')
        if query.strip():
            context['all_search_results'] = Recipe.objects.filter(name__icontains=query)
        else:
            context['all_search_results'] = None
        return context


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'dishly_app/recipes/details.html'
    context_object_name = 'recipe'


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'dishly_app/recipes/recipe_create.html'
    success_url = reverse_lazy("recipe-list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def handle_no_permission(self):
        return redirect('/')


class RecipeUpdateView(LoginRequiredMixin, UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'dishly_app/recipes/recipe_create.html'
    success_url = reverse_lazy("recipe-list")
    context_object_name = 'recipe'

    def handle_no_permission(self):
        return redirect('/')


class RecipeDeleteView(LoginRequiredMixin, DeleteView):
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



@login_required
def like_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    liked = False


    if request.user in recipe.likes.all():
        recipe.likes.remove(request.user)
    else:
        recipe.likes.add(request.user)
        liked = True


    if (
        request.headers.get('x-requested-with') == 'XMLHttpRequest'
        or request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
    ):
  
        return JsonResponse({
            'liked': liked,
            'total_likes': recipe.likes.count(),
        })

    return redirect('/')


def signup(request):
    error_message = ''
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/")

        error_message = ''  
    else:
        form = UserCreationForm()

    return render(request, "registration/signup.html", {
        'form': form,
        'error_message': error_message,
    })