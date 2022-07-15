from PIL import Image
from .crop_image import crop_image

"""
INPUT: List of starting item dictionaries
OUTPUT: URL of combined image of all the starting items from the dict
DESCRIPTION: Crops items from item sheet with Pillow, given positions. Combines cropped images.
"""

def create_starting_items_image(image_info_list) -> Image:
    final_image = Image.new('RGBA', (64 * 2, 64 * 1))
    images = map(crop_image, image_info_list)
    width = 0
    for image in images:
        final_image.paste(image, (width, 0))
        width += image.width
    return final_image
