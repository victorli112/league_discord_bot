from bs4 import BeautifulSoup

"""
INPUT: the soup object containing all information about skill priority
OUTPUT: a list of skill image links in recommended order
DESCRIPTION: get the recommended skill path of the champion
"""

def get_skill_priority(soup) -> list[str]:
    skill_priority = []
    for skill in soup.find_all('img'):
        skill_priority.append(skill['src'])
    return skill_priority