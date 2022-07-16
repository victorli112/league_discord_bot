"""
INPUT: the soup object containing all information about champion icon url
OUTPUT: a string of the champion icon url
DESCRIPTION: get the champion icon url
"""

def thumbnail_url(soup) -> str:
    return soup['src']
