from numpy import true_divide
import requests

from bs4 import BeautifulSoup

from get_build import get_build
from get_runes import get_runes

def get_blocks(champion_name: str, role: str):
    URL = f"https://www.metasrc.com/5v5/champion/lucian/{role}"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    search = [f"Best {champion_name} Summoner Spells",
            f"Best {champion_name} Starting Items",
            f"Best {champion_name} Runes",
            f"Best {champion_name} Item Build",
            f"Best {champion_name} Skill Order"]
    def matchSearch(text, search):
        return any(x in text for x in search)

    blocks = soup.find_all('div', class_ = "_yq1p7n")
    refined = []
    for block in blocks:
        # print(block.contents[0].text)
        # print(matchSearch(block.contents[0].text, search))
        if(matchSearch(block.contents[0].text, search)):
            refined.append(block)
            #print(block.contents[0].text)

    summoners = refined[0]
    starting = refined[1]
    runes = refined[2]
    build = refined[3]
    return refined

    #print(get_build(champion_name, role))

if __name__ == "__main__":
    blocks = get_blocks("Lucian", "adc")
    get_build(blocks[3])
