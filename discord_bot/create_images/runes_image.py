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
    final_image = Image.new('RGBA', (400, 128))
    row1_width = 0
    row2_width = 0
    row2_starting_height = 0

    for index, img_url in enumerate(runes.values()):
        response = requests.get(img_url)
        img = Image.open(BytesIO(response.content))
        # primary tree
        if index < 4:
            final_image.paste(img, (row1_width, 0))
            row1_width += img.width
            if row2_starting_height < img.height:
                row2_starting_height = img.height
        # secondary tree and perks
        else:
            # resize perks
            if index > 5:
                img = img.resize((math.floor(img.width * 1.3), math.floor(img.height * 1.3)))
            final_image.paste(img, (row2_width, row2_starting_height))
            row2_width += img.width
        img.close()
    return final_image