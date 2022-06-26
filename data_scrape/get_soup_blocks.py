import requests
from bs4 import BeautifulSoup

"""
INPUT: champion name: the name of the champion, has to be all lowercase
        role: the role of the champion, has to be all lowercase
OUTPUT: a list of soup objects partitioned by different aspects of a champion
DESCRIPTION: return blocks of information for a champion in a role
"""
def get_blocks(champion_name: str, role: str) -> list:
    if role == "":
        URL = f"https://www.metasrc.com/5v5/champion/{champion_name}"
    else:
        URL = f"https://www.metasrc.com/5v5/champion/{champion_name}/{role}"
        
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    search = [f"Best {champion_name.capitalize()} Summoner Spells",
            f"Best {champion_name.capitalize()} Starting Items",
            f"Best {champion_name.capitalize()} Runes",
            f"Best {champion_name.capitalize()} Item Build",
            f"Best {champion_name.capitalize()} Skill Order"]

    """ function to determine matching strings"""
    def matchSearch(text, search):
        return any(x == text for x in search)

    blocks = soup.find_all('div', class_ = "_yq1p7n")
    refined = []
    for block in blocks:
        if(matchSearch(block.contents[0].text, search)):
            refined.append(block)

    return refined