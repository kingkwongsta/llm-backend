from services.llm_json import generate_llm_response
from services.image_prompt import generate_image_prompt
from services.text_to_image import generate_image
from models.model_drink import DrinkRecipe
import json
import time


def generate_cocktail(prompt):
    start_time = time.perf_counter()
    recipe = json.loads(
        generate_llm_response(
            "openai", DrinkRecipe, "you are an expert mixologist", prompt
        )
    )
    image_prompt = json.loads(generate_image_prompt("openai", recipe))
    image = generate_image(image_prompt["prompt"])

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"Generation completed in {elapsed_time:.2f} seconds.")

    return {
        "recipe": recipe,
        "image": image["images"][0]["url"]
    }


# image out:  {'images': [{'url': 'https://fal.media/files/elephant/hJMm-7AQ31-aDWshs6NWY.png', 'width': 1024, 'height': 768, 'content_type': 'image/jpeg'}], 'timings': {'inference': 0.34091744339093566}, 'seed': 7468, 'has_nsfw_concepts': [False], 'prompt': "A beautifully crafted cocktail named 'Soju Sunrise', showcasing a tall glass filled with a vibrant, layered drink. The bottom layer is a deep red from grenadine, transitioning to a bright orange from fresh orange juice and pineapple juice, topped with a hint of green from a lime wheel garnish. The glass is filled with ice, and a sprinkle of chili powder is visible on top. The background features a sunny beach setting, with soft sand and gentle waves, evoking a refreshing and uplifting atmosphere, perfect for a sunny day or a lively gathering with friends."}
