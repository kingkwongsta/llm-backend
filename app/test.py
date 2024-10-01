import fal_client
from PIL import Image
import requests
from io import BytesIO


from dotenv import load_dotenv
import os

load_dotenv()

# Set your FAL AI API key
fal_client.api_key = os.getenv("FAL_API_KEY")


def generate_image(prompt):
    handler = fal_client.submit(
        "fal-ai/flux/schnell",
        arguments={"prompt": prompt},
    )

    result = handler.get()
    return result["image"]


def save_image(image_url, filename):
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))
    img.save(filename)
    print(f"Image saved as {filename}")


# Main execution
if __name__ == "__main__":
    prompt = 'Extreme close-up of a single tiger eye, direct frontal view. Detailed iris and pupil. Sharp focus on eye texture and color. Natural lighting to capture authentic eye shine and depth. The word "FLUX" is painted over it in big, white brush strokes with visible texture.'

    image_url = generate_image(prompt)
    save_image(image_url, "flux_generated_image.png")
