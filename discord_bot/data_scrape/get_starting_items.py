from bs4 import BeautifulSoup
import requests

"""
INPUT: the soup object containing all information about champion starting items
OUTPUT: a list consisting of dictionaries of the recommended starting items. {"sheet" : "blah, "position" : [x,y]}
DESCRIPTION: get the recommended starting items of the champion
"""
def get_starting_items(block) -> list:
    item_blocks = block.find_all(contains_background_image)
    items = list(map(convert_to_dict, item_blocks))
    return items

def contains_background_image(block):
    return block.has_attr('style') and "background-image" in block['style']

def convert_to_dict(element):
    element = str(element)
    # attributes = element.split(";")
    # sheet = attributes[2].split("(")[1][0:-1]
    # string_position = attributes[4].split(":")[1].split(" ")
    # position = [int(position[0:-2]) for position in string_position]
    sheet = element[element.find("https") : (element.find("webp") + 4)]
    string_position = element[element.find("background-position:") + 20 : element.find("zoom") - 1].split(" ")
    position = [abs(int(position[0:-2])) for position in string_position]
    return {"sheet": sheet, "position": position}

