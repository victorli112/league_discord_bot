from PIL import Image
from .crop_image import crop_image

"""
INPUT: List of list of build item dictionaries
OUTPUT: URL of combined image of all the build items from the dict
DESCRIPTION: Crops items from item sheet with Pillow, given positions. Combines cropped images.
"""

def create_build_image(build_list) -> Image:
    final_image = Image.new('RGBA', (64 * 6, 64 * 3))
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
            width += 64
            height = 0
    return final_image
