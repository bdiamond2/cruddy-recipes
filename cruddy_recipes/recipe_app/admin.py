from django.contrib import admin
from .models import Recipe, Ingredient, RecipeIngredient


@admin.register(Recipe, Ingredient, RecipeIngredient)
class ModelAdmin(admin.ModelAdmin):
    pass
