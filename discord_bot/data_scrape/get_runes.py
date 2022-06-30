#First page of runes at div id = 8000-8300-content
runePages = [
    {
        "keystone": "",
        "main_tree1": "",
        "main_tree2": "",
        "main_tree3": "",
        "secondary_tree1": "",
        "secondary_tree2": "",
        "secondary_tree3": "",
        "shard_1": "",
        "shard_2": "",
        "shard_3": "",
    },
    {
        "keystone": "",
        "main_tree1": "",
        "main_tree2": "",
        "main_tree3": "",
        "secondary_tree1": "",
        "secondary_tree2": "",
        "secondary_tree3": "",
        "shard_1": "",
        "shard_2": "",
        "shard_3": "",
    },
    {
        "keystone": "",
        "main_tree1": "",
        "main_tree2": "",
        "main_tree3": "",
        "secondary_tree1": "",
        "secondary_tree2": "",
        "secondary_tree3": "",
        "shard_1": "",
        "shard_2": "",
        "shard_3": "",
    },
    {
        "keystone": "",
        "main_tree1": "",
        "main_tree2": "",
        "main_tree3": "",
        "secondary_tree1": "",
        "secondary_tree2": "",
        "secondary_tree3": "",
        "shard_1": "",
        "shard_2": "",
        "shard_3": "",
    },
]

"""
INPUT: the soup object containing all information about champion runes
OUTPUT: a dictionary consisting of all the runes that is recommended.
            NOTE: there are 4 sets of runes
DESCRIPTION: get the recommended runes of the champion
"""
def get_runes(soup) -> dict:
    # runes = soup.find_all('div', class_ = "_3goykt _hmag7l tooltipped")
    allRunes = soup.find_all('image', class_ = "lozad")
    runes = allRunes[8 : ]
    i = 0
    for page in runePages:
        for x,y in page.items():
            page[x] = runes[i]['data-xlink-href']
            i += 1
    return runePages
    
    # for page in runePages:
    #     print(page)