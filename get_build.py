from bs4 import BeautifulSoup
import requests

"""
INPUT: champion_name: the champion to be queried
        role: the role of the champion
OUTPUT: a dictionary consisting of all the items that is recommended.
            NOTE: item_0 are the boots, item_6 is the ward, item_7 is the elixir. The other items are listed chronologically.
DESCRIPTION: get the recommended build of the champion in the role
"""
def get_build(champion_name: str, role: str) -> dict:
    url = f"https://www.metasrc.com/5v5/champion/{champion_name}/{role}"
    req = requests.get(url=url)
    soup = BeautifulSoup(req.content, 'html.parser')
    
    items ={}
    counter = 0

    for i in soup.find_all('div', {'class' : ['_5lds7o-3 _82gy0d', '_5lds7o-1 _82gy0d']}):
        img = i.find('img')
        item = img['alt']
        items[f'item_{counter}'] = item
        counter += 1

    return items

get_build("azir", "mid")