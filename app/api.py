from fastapi import FastAPI, Query

# from fastapi.middleware.cors import CORSMiddleware
from services.llm_json import generate_llm_response
# from services.text_to_image import generate_image
# from services.image_prompt import generate_image_prompt
from services.cocktail import generate_cocktail
from models.model_drink import DrinkRecipe
import json

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World WORLD"}


@app.get("/llm_json")
async def get_response(
    llm_model: str = Query(default="openai"),
    JSON_format: str = Query(default="drink"),
    system: str = Query(default=None),
    user: str = Query(default=None),
):
    # async def get_cocktail(liquor: str = Query(default=None), flavor: str = Query(default=None), mood: str = Query(default=None)):
    if JSON_format == "drink":
        format = DrinkRecipe
    response = json.loads(generate_llm_response(llm_model, format, system, user))
    return response


# @app.get("/text_to_image")
# async def get_image(prompt: str = Query(default=None)):
#     response = generate_image(prompt)
#     return response["images"][0]["url"]


# @app.get("/image_prompt")
# async def get_image_prompt(input: str = Query(default=None)):
#     response = json.loads(generate_image_prompt("openai", input))
#     return response


@app.get("/generate_cocktail")
async def get_cockatil(prompt: str = Query(default=None)):
    response = generate_cocktail(prompt)
    return response
