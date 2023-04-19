from dishes.services import Dishes


def get_dish_action(dish_id: int):
    return Dishes.get_dish(dish_id)
