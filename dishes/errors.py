from app.errors import FoodFactoryError


class DishError(FoodFactoryError):
    ...


class DishNotFound(DishError):
    ...
