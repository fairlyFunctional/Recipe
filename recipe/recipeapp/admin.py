from django.contrib import admin
from recipeapp.models import Recipe, Category, Ingredient, IngredientAmount

admin.site.register(Ingredient)
admin.site.register(IngredientAmount)
admin.site.register(Recipe)
admin.site.register(Category)