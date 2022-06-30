from .get_build import get_build
from .get_soup_blocks import get_blocks
from .get_runes import get_runes
from .get_starting_items import get_starting_items
from .get_skills import get_skills
from .get_summoner_spells import get_summoner_spells

class ResponseStruct():
    def __init__(self, runes, summoners, skills, starting_items, build):
        self.runes = runes
        self.summoners = summoners
        self.skills = skills
        self.starting_items = starting_items
        self.build = build

def get_information(champion_name: str, role: str=""):
    blocks = get_blocks(champion_name, role)
    runes = get_runes(blocks[0])
    summoners = get_summoner_spells(blocks[1])
    skills = get_skills(blocks[2])
    starting_items = get_starting_items(blocks[3])
    build = get_build(blocks[4])
    response = ResponseStruct(runes, summoners, skills, starting_items, build)
    return(response)