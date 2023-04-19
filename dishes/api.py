from ninja import Router
from ninja.responses import codes_4xx

from app.schema import Error
from dishes.errors import DishNotFound
from dishes.use_cases.get_dish.action import get_dish_action
from dishes.use_cases.get_dish.schemas import Dish


dishes_router = Router()


@dishes_router.get('/{int:dish_id}', response={
    200: Dish,
    codes_4xx: Error,
})
def get_dish(request, dish_id: int):
    try:
        return get_dish_action(dish_id)
    except DishNotFound:
        return 404, {'message': 'Dish not found'}
