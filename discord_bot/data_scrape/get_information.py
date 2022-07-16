from .get_build import get_build
from .get_soup_blocks import get_blocks
from .get_runes import get_runes
from .get_starting_items import get_starting_items
from .get_skill_priority import get_skill_priority
from .get_skills import get_skills
from .get_summoner_spells import get_summoner_spells
from .get_thumbnail_url import get_thumbnail_url

class ResponseStruct():
    def __init__(self, thumbnail_url, runes, summoners, skill_priority, skills, starting_items, build):
        self.thumbnail_url = thumbnail_url
        self.runes = runes
        self.summoners = summoners
        self.skill_priority = skill_priority
        self.skills = skills
        self.starting_items = starting_items
        self.build = build

def get_information(champion_name: str, role: str=""):
    blocks = get_blocks(champion_name, role)
    thumbnail_url = get_thumbnail_url(blocks[0])
    runes = get_runes(blocks[1])
    summoners = get_summoner_spells(blocks[2])
    skill_priority = get_skill_priority(blocks[3])
    skills = get_skills(blocks[4])
    starting_items = get_starting_items(blocks[5])
    build = get_build(blocks[6], blocks[7], blocks[8], blocks[9])
    response = ResponseStruct(url, runes, summoners, skill_priority, skills, starting_items, build)
    return(response)