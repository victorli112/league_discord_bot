"""
INPUT: the soup object containing all information about summoner spells
OUTPUT: a dictionary consisting of all the summoner spells that is recommended.
            NOTE: the first two are the most used. Subsequent ones may be swapped
DESCRIPTION: get the recommended summoner spells of the champion
"""

def get_summoner_spells(soup) -> dict:
    spells = {}
    allSpells = soup.find_all('img', class_ = 'lozad')
    i = 0
    for spell in allSpells:
        spells[i] = spell['data-src']
        i += 1
    
    return spells