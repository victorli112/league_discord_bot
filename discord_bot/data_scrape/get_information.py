from .get_build import get_build
from .get_soup_blocks import get_blocks
from .get_runes import get_runes
from .get_starting_items import get_starting_items
from .get_skills import get_skills
from .get_summoner_spells import get_summoner_spells

def get_information(champion_name: str, role: str):
    blocks = get_blocks(champion_name, role)
    runes = get_runes(blocks[2])
    build = get_build(blocks[3])
    summoners = get_summoner_spells(blocks[0])
    starting_items = get_starting_items(blocks[1])
    skills = get_skills(blocks[4])
    return(summoners)