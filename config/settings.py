from typing import Optional
from pydantic_settings import BaseSettings
from functools import lru_cache
from dotenv import load_dotenv
import os

load_dotenv()


class LLMProviderSettings(BaseSettings):
    temperature: float = 0.0
    max_tokens: Optional[int] = None
    max_retries: int = 3


class OpenAISettings(LLMProviderSettings):
    api_key: str = os.getenv("OPENAI_API_KEY")
    default_model: str = "gpt-4o-mini-2024-07-18"


class AnthropicSettings(LLMProviderSettings):
    api_key: str = os.getenv("ANTHROPIC_API_KEY")
    default_model: str = "claude-3-5-sonnet-20240620"
    max_tokens: int = 1024


class Settings(BaseSettings):
    app_name: str = "GenAI Project Template"
    openai: OpenAISettings = OpenAISettings()
    anthropic: AnthropicSettings = AnthropicSettings()


@lru_cache
def get_settings():
    return Settings()
