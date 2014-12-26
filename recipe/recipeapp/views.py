from django.shortcuts import render, get_object_or_404
from django.template import RequestContext, loader
from django.http import Http404
from recipeapp.models import Recipe, Category
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.core.urlresolvers import reverse_lazy

def index(request):
	latest_recipe_list = Recipe.objects.order_by('name')[:5]
	category_list = Category.objects.all()
	context = {'latest_recipe_list': latest_recipe_list,'category_list': category_list}
	return render(request, 'recipe/index.html', context)

# Create your views here.

def detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'recipe/detail.html', {'recipe': recipe})

class RecipeCreate(CreateView):
    model = Recipe
    fields = ['name']

class RecipeUpdate(UpdateView):
    model = Recipe
    fields = ['name','author','category','ingredients','directions','photo']

class RecipeDelete(DeleteView):
    model = Recipe
    success_url = reverse_lazy('recipe:index')

#def edit(request, recipe_id):
	#recipe = get_object_or_404(Recipe, pk=recipe_id)
	#return render(request, 'recipe/edit.html', {'recipe': recipe})

def list(request, category_id):
	category = get_object_or_404(Category, pk=category_id)
	return render(request, 'category/list.html', {'category': category,})