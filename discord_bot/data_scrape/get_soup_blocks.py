import os
from selenium import webdriver
from bs4 import BeautifulSoup
from utils import get_link

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

"""
INPUT: champion name: the name of the champion, has to be all lowercase
        role: the role of the champion, has to be all lowercase, could be empty
OUTPUT: a list of soup objects partitioned by different aspects of a champion
DESCRIPTION: return blocks of information for a champion in a role
    NOTE: 0 - champion icon url
          1 - runes
          2 - summoner spells
          3 - skill priority
          4 - skill path
          5 - starting items
          6 - first 3 items
          7 - fourth item options
          8 - fifth item options
          9 - sixth item options
"""

def get_blocks(champion_name: str, role: str ="") -> list:
    URL = get_link(champion_name, role)
    driver.get(URL)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    classes = [
        'champion-image',
        'content-section_content recommended-build_runes',
        'content-section_content summoner-spells',
        'content-section_content skill-priority',
        'content-section_content skill-path-block',
        'content-section_content starting-items',
        'content-section_content core-items mythic-border-container',
        'content-section_content item-options item-options-1',
        'content-section_content item-options item-options-2',
        'content-section_content item-options item-options-3',
    ]

    blocks = soup.find_all(True, {'class':classes})
    return blocks