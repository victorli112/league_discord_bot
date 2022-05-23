#First page of runes at div id = 8000-8300-content
runepage1 = {
    "keystone": "",
    "main_tree1": "",
    "main_tree2": "",
    "main_tree3": "",
    "secondary_tree1": "",
    "secondary_tree2": "",
    "secondary tree3": ""
}

runepage2 = {
    "keystone": "",
    "main_tree1": "",
    "main_tree2": "",
    "main_tree3": "",
    "secondary_tree1": "",
    "secondary_tree2": "",
    "secondary tree3": ""
}

runepage3 = {
    "keystone": "",
    "main_tree1": "",
    "main_tree2": "",
    "main_tree3": "",
    "secondary_tree1": "",
    "secondary_tree2": "",
    "secondary tree3": ""
}

runepage4 = {
    "keystone": "",
    "main_tree1": "",
    "main_tree2": "",
    "main_tree3": "",
    "secondary_tree1": "",
    "secondary_tree2": "",
    "secondary tree3": ""
}
def get_runes(soup):
    # runes = soup.find_all('div', class_ = "_3goykt _hmag7l tooltipped")
    allRunes = soup.find_all('image', class_ = "lozad")
    runes = allRunes[8 : ]
    for rune in runes:
        print(rune['data-xlink-href'])
