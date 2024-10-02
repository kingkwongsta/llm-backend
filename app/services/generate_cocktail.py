from llm_json import generate_llm_response
from image_prompt import generate_image_prompt
from models.model_drink import DrinkRecipe
import json


def generate_cocktail(prompt):
    recipe = json.loads(
        generate_llm_response(
            "openai", DrinkRecipe, "you are an expert mixologist", prompt
        )
    )
    # recipe_prompt_prepare = recipe.name, recipe.d
    image_prompt = generate_image_prompt("openai", recipe)
    return image_prompt


print(generate_cocktail("create me a creative and unique drink with soju"))
