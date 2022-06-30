from bs4 import BeautifulSoup
import requests

"""
INPUT: the soup object containing all information about champion build
OUTPUT: a dictionary consisting of all the items that is recommended.
            NOTE: item_6 is the ward, item_7 is the elixir. The other items are listed chronologically.
DESCRIPTION: get the recommended build of the champion
"""
def get_build(blocks) -> dict:
    items = {}
    counter = 0

    for i in blocks.find_all('div', {'class' : ['_5lds7o-3 _82gy0d', '_5lds7o-1 _82gy0d']}):
        img = i.find('img')
        item_data = []
        item_data.append(img['data-src'])
        item_data.append(img['alt'])
        items[f'item_{counter}'] = item_data
        counter += 1
    return items
