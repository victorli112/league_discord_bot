#First page of runes at div id = 8000-8300-content
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

"""
INPUT: the soup object containing all information about champion runes
OUTPUT: a dictionary consisting of all the runes that is recommended.
DESCRIPTION: get the recommended runes of the champion
"""
def get_runes(soup) -> dict:
    test = []
    for active_runes in soup.find_all('div', {'class':['shard-active', 'perk-active']}):
        test.append(active_runes.find('img')['src'])
    for i, k in enumerate(runePage.keys()):
        runePage[k] = test[i]
    return(runePage)
    