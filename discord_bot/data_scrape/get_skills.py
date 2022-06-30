from bs4 import BeautifulSoup
import requests

"""
INPUT: the soup object containing all information about champion build
OUTPUT: a dictionary consisting of all the items that is recommended.
DESCRIPTION: get the recommended build of the champion
"""
def get_skills(blocks) -> list:
    possible_skills = ['q','w','e','r']
    skills = [""] * 18

    # first find each row
    skill_num = 0
    for i in blocks.find_all('div', {'class' : ['skill-order']}):
        for j in i.find_all('div', {'class': ['skill-up']}):
            level = int(j.find('div').text) - 1
            skills[level] = possible_skills[skill_num]
        skill_num += 1
    return skills


