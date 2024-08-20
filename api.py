from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from services.llm_json import generate_llm_response
from typing import List, Type
from models.model_drink import DrinkRecipe
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


# TESTING OPENAI
@app.get("/llm_json")
async def get_response(
    llm_model: str = Query(default="openai"),
    JSON_format: str = Query(default=None),
    system: str = Query(default=None),
    user: str = Query(default=None),
):
    # async def get_cocktail(liquor: str = Query(default=None), flavor: str = Query(default=None), mood: str = Query(default=None)):
    if JSON_format == "drink":
        format = DrinkRecipe
    response = json.loads(generate_llm_response(llm_model, format, system, user))
    return response
