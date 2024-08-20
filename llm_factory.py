from typing import Any, Dict, List, Type
import json
import instructor
from anthropic import Anthropic
from config.settings import get_settings
from openai import OpenAI
from pydantic import BaseModel, Field
from models.model_drink import DrinkRecipe


class LLMFactory:
    def __init__(self, provider: str):
        self.provider = provider
        self.settings = getattr(get_settings(), provider)
        self.client = self._initialize_client()

    def _initialize_client(self) -> Any:
        client_initializers = {
            "openai": lambda s: instructor.from_openai(OpenAI(api_key=s.api_key)),
            "anthropic": lambda s: instructor.from_anthropic(
                Anthropic(api_key=s.api_key)
            ),
            "llama": lambda s: instructor.from_openai(
                OpenAI(base_url=s.base_url, api_key=s.api_key),
                mode=instructor.Mode.JSON,
            ),
        }

        initializer = client_initializers.get(self.provider)
        if initializer:
            return initializer(self.settings)
        raise ValueError(f"Unsupported LLM provider: {self.provider}")

    def create_completion(
        self, response_model: Type[BaseModel], messages: List[Dict[str, str]], **kwargs
    ) -> Any:
        completion_params = {
            "model": kwargs.get("model", self.settings.default_model),
            "temperature": kwargs.get("temperature", self.settings.temperature),
            "max_retries": kwargs.get("max_retries", self.settings.max_retries),
            "max_tokens": kwargs.get("max_tokens", self.settings.max_tokens),
            "response_model": response_model,
            "messages": messages,
        }
        return self.client.chat.completions.create(**completion_params)


if __name__ == "__main__":

    liquor = "Vodka"
    flavor = "Sweet"
    mood = "Happy"
    messages = [
        {
            "role": "system",
            "content": "You are a helpful mixologist designed to output JSON.",
        },
        {
            "role": "user",
            "content": " f'''Create a unique creative advanced cocktail recipe based on the following user preferences of {liquor}, {flavor}, {mood}.  Name the drink something creative with a lot of variability and uniquess.",
        },
    ]

    llm = LLMFactory("openai")
    completion = llm.create_completion(
        response_model=DrinkRecipe,
        messages=messages,
    )
    assert isinstance(completion, DrinkRecipe)

    print(completion.json())
    # print(f"name: {completion.name}\n")
    # print(f"description: {completion.description}")
