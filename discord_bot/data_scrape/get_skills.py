from bs4 import BeautifulSoup
import requests

"""
INPUT: the soup object containing all information about champion build
OUTPUT: a dictionary consisting of all the items that is recommended.
DESCRIPTION: get the recommended build of the champion
"""
def get_skills(blocks) -> list:
    skills = [""] * 19

    # first find each row
    for i in blocks.find_all('tr', {'class' : ['_sbzxum']}):
        counter = 0
        for j in i.find_all('td'):
            # if its not a number
            if not j.text.isdigit():
                if j.text != "":
                    skills[counter] = j.text
            counter += 1
    return skills[1:]


