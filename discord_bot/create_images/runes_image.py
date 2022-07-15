from PIL import Image
import requests
import math
from io import BytesIO

"""
INPUT: Runes dictionary from ResponseStruct object
OUTPUT: URL of combined image of all the rune urls from the dict
DESCRIPTION: Converts urls to images with BytesIO. Combine images with Pillow. Combined image used for embed.
"""
def create_rune_image(runes) -> Image:
    final_image = Image.new('RGBA', (64 * 5, 64 * 2))
    row1_width = 0
    row2_width = 0
    row2_starting_height = 0

    for index, img_url in enumerate(runes.values()):
        response = requests.get(img_url)
        image = Image.open(BytesIO(response.content))
        image = image.resize((64, 64))
        # primary tree
        if index < 4:
            final_image.paste(image, (row1_width, 0))
            row1_width += image.width
            if row2_starting_height < image.height:
                row2_starting_height = image.height
        # secondary tree and perks
        else:
            final_image.paste(image, (row2_width, row2_starting_height))
            row2_width += image.width
        image.close()
    return final_image