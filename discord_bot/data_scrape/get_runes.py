"""
INPUT: the soup object containing all information about champion runes
OUTPUT: a dictionary consisting of all the runes that is recommended.
DESCRIPTION: get the recommended runes of the champion
"""
def get_runes(soup) -> dict:
    runePage = {
        "keystone": "",
        "main_tree1": "",
        "main_tree2": "",
        "main_tree3": "",
        "secondary_tree1": "",
        "secondary_tree2": "",
        "shard_1": "",
        "shard_2": "",
        "shard_3": "",
    }
    runes = []

    # get all the runes
    for active_runes in soup.find_all('div', {'class':['shard-active', 'perk-active']}):
        runes.append(active_runes.find('img')['src'])

    # map all the runes to the runePage dictionary
    for i, k in enumerate(runePage.keys()):
        runePage[k] = runes[i]
    return(runePage)
    