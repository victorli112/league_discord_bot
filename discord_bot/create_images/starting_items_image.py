from PIL import Image
import requests
from io import BytesIO

"""
INPUT: List of starting item dictionaries
OUTPUT: URL of combined image of all the starting items from the dict
DESCRIPTION: Crops items from item sheet with Pillow, given positions. Combines cropped images.
"""

def create_starting_items_image(image_info_list) -> Image:
    final_image = Image.new('RGBA', (48 * 2, 48 * 1))
    images = map(crop_image, image_info_list)
    width = 0
    for image in images:
        final_image.paste(image, (width, 0))
        width += image.width
    return final_image

def crop_image(image_info):
    response = requests.get(image_info['sheet'])
    sheet_image = Image.open(BytesIO(response.content))
    width = image_info['position'][0]
    height = image_info['position'][1]
    area = (width, height, (width + 48), (height + 48))
    starting_item = sheet_image.crop(area)
    sheet_image.close()
    return starting_item
