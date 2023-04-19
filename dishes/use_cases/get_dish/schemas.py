from typing import List

from ninja import Schema


class Ingredient(Schema):
    name: str
    calories: float

    class Config:
        orm_mode = True


class Dish(Schema):
    id: int
    name: str
    description: str
    ingredients: List[Ingredient]

    class Config:
        orm_mode = True
