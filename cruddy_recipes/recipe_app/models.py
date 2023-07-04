from django.db import models


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    ingredients = models.ManyToManyField(
        'Ingredient', through='RecipeIngredient')
    description = models.TextField(default='')

    def __str__(self):
        return self.title


class Ingredient(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    unit = models.CharField(max_length=50)
    amount = models.FloatField(default=0.0)

    def __str__(self):
        return f'{self.recipe} - {self.ingredient} ({self.unit} {self.amount})'
