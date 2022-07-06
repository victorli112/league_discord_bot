from .get_build import get_build
from .get_soup_blocks import get_blocks
from .get_runes import get_runes
from .get_starting_items import get_starting_items
from .get_skill_priority import get_skill_priority
from .get_skills import get_skills
from .get_summoner_spells import get_summoner_spells

class ResponseStruct():
    def __init__(self, runes, summoners, skill_priority, skills, starting_items, build):
        self.runes = runes
        self.summoners = summoners
        self.skill_priority = skill_priority
        self.skills = skills
        self.starting_items = starting_items
        self.build = build

def get_information(champion_name: str, role: str=""):
    blocks = get_blocks(champion_name, role)
    runes = get_runes(blocks[0])
    summoners = get_summoner_spells(blocks[1])
    skill_priority = get_skill_priority(blocks[2])
    skills = get_skills(blocks[3])
    starting_items = get_starting_items(blocks[4])
    build = get_build(blocks[5], blocks[6], blocks[7], blocks[8])
    response = ResponseStruct(runes, summoners, skill_priority, skills, starting_items, build)
    return(response)