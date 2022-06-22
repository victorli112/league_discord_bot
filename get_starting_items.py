from bs4 import BeautifulSoup
import requests

"""
INPUT: the soup object containing all information about champion starting items
OUTPUT: a dictionary consisting of all the items that is recommended.
DESCRIPTION: get the recommended starting items of the champion
"""
def get_starting_items(blocks) -> dict:
    items = {}
    counter = 0

    for i in blocks.find_all('div', {'class' : ['_5lds7o-3', '_dtoou _iqcim1 _dcqhsp']}):
        img = i.find('img')
        item_data = []
        item_data.append(img['data-src'])
        item_data.append(img['alt'])
        if counter > 0:
            items[f'item_{counter - 1}'] = item_data
        counter += 1
    return items
