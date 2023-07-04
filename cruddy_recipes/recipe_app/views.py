from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Recipe


def hello_world(request):
    return HttpResponse('hello world')


def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe_app/recipe_list.html', {'recipes': recipes})


def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    recipe_ingredients = recipe.recipeingredient_set.all()
    return render(request, 'recipe_app/recipe_detail.html', {'recipe': recipe, 'recipe_ingredients': recipe_ingredients})
