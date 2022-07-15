from PIL import Image

"""
INPUT: List of image file names
OUTPUT: Image of all files combined
DESCRIPTION: Create the final image with runes, build, starting items, and summoners
"""
def build_final_image(image_list: list) -> Image:
    final_image = Image.open('bot template.png')
    coord_list = [(2,46), (354,46), (2,238), (226,238), (2,366)]
    for image, coords in zip(image_list, coord_list):
        img = Image.open(image)
        img_copy = img.copy()
        final_image.paste(img_copy, coords)
    return final_image
