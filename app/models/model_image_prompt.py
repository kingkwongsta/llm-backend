from pydantic import BaseModel
from typing import List


class ImagePrompt(BaseModel):
    prompt: str
