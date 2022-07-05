from PIL import Image
import requests
from io import BytesIO

"""
INPUT: List of summoner spell urls
OUTPUT: URL of combined image of all the starting items from the dict
DESCRIPTION: Crops items from item sheet with Pillow, given positions. Combines cropped images.
"""

def create_summoner_spells_image(spell_list):
    final_image = Image.new('RGBA', (64 * 2, 64 * 1))
    width = 0
    for spell_url in spell_list:
        response = requests.get(spell_url)
        img = Image.open(BytesIO(response.content))
        final_image.paste(img, (width, 0))
        width += img.width
    return final_image