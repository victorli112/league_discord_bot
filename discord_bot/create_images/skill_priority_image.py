from PIL import Image
import requests
from io import BytesIO

"""
INPUT: List of skill urls
OUTPUT: URL of combined image of the skill path
DESCRIPTION: Crops items from item sheet with Pillow, given positions. Combines cropped images.
"""

def create_skill_priority_image(skills) -> Image:
    final_image = Image.new('RGBA', (64 * 3, 64 * 1))
    width = 0
    for skill_url in skills:
        response = requests.get(skill_url)
        image = Image.open(BytesIO(response.content))
        image = image.resize((64, 64))
        final_image.paste(image, (width, 0))
        width += image.width
    return final_image
