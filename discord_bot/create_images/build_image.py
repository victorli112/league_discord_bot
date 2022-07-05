from PIL import Image
import requests
from io import BytesIO

"""
INPUT: List of list of build item dictionaries
OUTPUT: URL of combined image of all the build items from the dict
DESCRIPTION: Crops items from item sheet with Pillow, given positions. Combines cropped images.
"""

def create_build_image(build_list) -> Image:
    final_image = Image.new('RGBA', (48 * 6, 48 * 3))
    width = 0
    height = 0
    for slot_options in build_list:
        images = map(crop_image, slot_options)
        if width == 0:
            for image in images:
                final_image.paste(image, (width, 0))
                width += image.width
        else:
            for image in images:
                final_image.paste(image, (width, height))
                height += image.height
            width += 48
            height = 0
    return final_image

def crop_image(image_info):
    response = requests.get(image_info['sheet'])
    sheet_image = Image.open(BytesIO(response.content))
    width = image_info['position'][0]
    height = image_info['position'][1]
    area = (width, height, (width + 48), (height + 48))
    build_item = sheet_image.crop(area)
    sheet_image.close()
    return build_item