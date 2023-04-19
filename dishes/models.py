from typing import List

from django.db import models
from django.utils import timezone


class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    calories_per_100g = models.FloatField()
    created_at = models.DateTimeField(default=timezone.now)

    @property
    def calories(self):
        return self.calories_per_100g

    class Meta:
        db_table = 'ingredients'

    def __str__(self):
        return self.name


class Recipe(models.Model):
    ingredients = models.ManyToManyField(
        Ingredient,
        through='RecipeIngredient',
        through_fields=('recipe', 'ingredient'),
    )
    name = models.CharField(max_length=255)
    notes = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'recipes'

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity_grams = models.FloatField()
    quantity_label = models.CharField(max_length=16)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'recipe_ingredients'

    def __str__(self):
        return self.ingredient.name


class RecipeStep(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    instructions = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'recipe_steps'

    def __str__(self):
        return '{} > {}'.format(self.recipe.name, self.ingredient.name)


class Dish(models.Model):
    recipe = models.OneToOneField(Recipe, on_delete=models.CASCADE)
    public_id = models.CharField(max_length=16)
    name = models.CharField(max_length=255)
    description = models.TextField()
    daily_limit = models.FloatField()
    created_at = models.DateTimeField(default=timezone.now)

    @property
    def ingredients(self) -> List[Ingredient]:
        return self.recipe.ingredients.all()

    class Meta:
        db_table = 'dishes'

    def __str__(self):
        return self.name
