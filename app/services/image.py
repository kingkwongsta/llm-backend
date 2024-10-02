import fal_client
import random
from dotenv import load_dotenv
import os

load_dotenv()
fal_client.api_key = os.getenv("FAL_KEY")


def generate_image(prompt):
    handler = fal_client.submit(
        "fal-ai/flux/schnell",
        arguments={
            "prompt": prompt,
            "seed": random.randint(1, 100000),
            "image_size": "landscape_4_3",
            "num_images": 1,
        },
    )

    result = handler.get()
    print(result)
    return result
