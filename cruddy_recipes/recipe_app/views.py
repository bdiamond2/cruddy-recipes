from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe


def hello_world(request):
    return HttpResponse('hello world')


def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe_app/recipe_list.html', {'recipes': recipes})
