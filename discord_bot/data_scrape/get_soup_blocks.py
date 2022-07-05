import requests
from bs4 import BeautifulSoup

"""
INPUT: champion name: the name of the champion, has to be all lowercase
        role: the role of the champion, has to be all lowercase
OUTPUT: a list of soup objects partitioned by different aspects of a champion
DESCRIPTION: return blocks of information for a champion in a role
    NOTE: 0 - runes
          1 - summoner spells
          2 - skill path
          3 - starting items
          4 - first three items
          5 - fourth item options
          6 - fifth item options
          7 - sixth item options
"""
def get_blocks(champion_name: str, role: str ="") -> list:
    if role == "":
        URL = f"https://u.gg/lol/champions/{champion_name}/build"
    else:
        URL = f"https://u.gg/lol/champions/{champion_name}/build?role={role}"
        
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    classes = [
        'content-section_content recommended-build_runes',
        'content-section_content summoner-spells',
        'content-section_content skill-path-block',
        'content-section_content starting-items',
        'content-section_content core-items mythic-border-container',
        'content-section_content item-options item-options-1',
        'content-section_content item-options item-options-2',
        'content-section_content item-options item-options-3'
    ]

    blocks = soup.find_all(True, {'class':classes})
    return blocks[:8]
