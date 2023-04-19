from django.contrib import admin
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Dish, RecipeIngredient, Ingredient, Recipe, RecipeStep
from .producers import publish_dish_created, publish_dish_updated


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    exclude = ['created_at']


class RecipeIngredientInline(admin.StackedInline):
    exclude = ['created_at']
    model = RecipeIngredient
    extra = 1


class RecipeStepInline(admin.StackedInline):
    exclude = ['created_at']
    model = RecipeStep
    extra = 1


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'notes')
    exclude = ['created_at']
    inlines = [
        RecipeIngredientInline,
        RecipeStepInline,
    ]


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'public_id', 'daily_limit')
    exclude = ['created_at']


@receiver(post_save, sender=Dish)
def on_dish_save(**kwargs):
    dish_id = kwargs['instance'].pk

    if kwargs['created']:
        publish_dish_created(dish_id)
    else:
        publish_dish_updated(dish_id)
