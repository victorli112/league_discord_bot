from get_soup_blocks import get_blocks
from get_build import get_build
from get_runes import get_runes
from get_summoner_spells import get_summoner_spells

if __name__ == "__main__":
    blocks = get_blocks("lucian", "adc")
    runes = get_runes(blocks[2])
    build = get_build(blocks[3])
    summoners = get_summoner_spells(blocks[0])

    """
    rest of function will look something like:
    summoners = get_summoners(blocks[0])
    starting_items = get_starting_items(blocks[1])
    skills = get_skills(blocks[4])
    
    then we will try to pass all this into to the discord bot to display
    """

print(summoners)