from pydantic import BaseModel, Field
from typing import List


class IngredientItem(BaseModel):
    name: str
    quantity: str


class DrinkRecipe(BaseModel):
    name: str
    description: str
    ingredients: List[IngredientItem]
    instructions: List[str]
    drink_feeling: str = Field(
        description="The feeling/mood that the drink evokes including a settings"
    )


class Drink(BaseModel):
    user_flavor: str
    user_mood: str
    user_liquor: str
    drink_recipe: DrinkRecipe
    drink_image: str
