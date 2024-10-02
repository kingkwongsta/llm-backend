from pydantic import BaseModel, Field


class ImagePrompt(BaseModel):
    prompt: str = Field(description="The text to image prompt to generate an image")
