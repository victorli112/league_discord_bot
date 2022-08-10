"""
INPUT: the soup object containing all information about champion starting items
OUTPUT: a list consisting of dictionaries of the recommended starting items. {"sheet" : "img link", "position" : [x,y]}
DESCRIPTION: get the recommended starting items of the champion
"""
def get_starting_items(block) -> list[dict]:
    item_blocks = block.find_all(contains_background_image)
    print(item_blocks)
    items = list(map(convert_to_dict, item_blocks))
    return items

def contains_background_image(block) -> bool:
    return block.has_attr('style') and "background-image" in block['style']

def convert_to_dict(element) -> dict:
    element = str(element)
    sheet = element[element.find("https") : (element.find("webp") + 4)]
    bg_pos = element.find("background-position")
    pos_start = element.find(":", bg_pos) + 1
    pos_end = element.find(";", bg_pos)
    string_position = element[pos_start : pos_end].strip().split(" ")
    position = [abs(int(position[0:-2])) for position in string_position]
    return {"sheet": sheet, "position": position}

