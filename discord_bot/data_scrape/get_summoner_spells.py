"""
INPUT: the soup object containing all information about summoner spells
OUTPUT: a list of image links of the summoner spells that are recommended
DESCRIPTION: get the recommended summoner spells of the champion
"""

def get_summoner_spells(soup) -> list[str]:
    spells = []
    for i in soup.find_all('img'):
        spells.append(i['src'])
    return spells