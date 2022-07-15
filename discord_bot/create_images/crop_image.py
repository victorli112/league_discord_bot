from PIL import Image
import requests
from io import BytesIO

def crop_image(image_info):
    response = requests.get(image_info['sheet'])
    sheet_image = Image.open(BytesIO(response.content))
    width = image_info['position'][0]
    height = image_info['position'][1]
    area = (width, height, (width + 48), (height + 48))
    starting_item = sheet_image.crop(area)
    starting_item = starting_item.resize((64, 64))
    sheet_image.close()
    return starting_item