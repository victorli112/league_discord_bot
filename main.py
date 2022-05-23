import requests
from bs4 import BeautifulSoup

import get_runes
def main():
    URL = "https://www.metasrc.com/5v5/champion/lucian/adc"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    search = ["Summoner Spells", "Starting Items", "Runes", "Item Build", "Skill Order"]
    def matchSearch(text, search):
        if any(x in text for x in search):
            return True
        else:
            return False

    blocks = soup.find_all('div', class_ = "_yq1p7n")
    refined = []
    for block in blocks:
        # print(block.contents[0].text)
        # print(matchSearch(block.contents[0].text, search))
        if(matchSearch(block.contents[0].text, search)):
            refined.append(block)

    summoners = refined[0]
    starting = refined[1]
    runes = refined[2]

    get_runes.get_runes(runes)

if __name__ == "__main__":
    main()