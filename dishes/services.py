from django.core.exceptions import ObjectDoesNotExist

from dishes.errors import DishNotFound
from dishes.models import Dish


class Dishes:
    @staticmethod
    def get_dish(dish_id: int) -> Dish:
        try:
            return Dish.objects.get(pk=dish_id)
        except ObjectDoesNotExist:
            raise DishNotFound('Dish with given Id was not found')
