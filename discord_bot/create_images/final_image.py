from PIL import Image

"""
INPUT: List of image file names
OUTPUT: Image of all files combined
DESCRIPTION: Create the final image with runes, build, starting items, and summoners
"""
def build_final_image(image_list: list) -> Image:
    final_image = Image.new('RGBA',(48 * 6, 64 + 64 + 64 + (48 * 4)))
    height = 0
    for image in image_list:
        img = Image.open(image)
        img_copy = img.copy()
        final_image.paste(img_copy, (0, height))
        height += img_copy.height
    return final_image
