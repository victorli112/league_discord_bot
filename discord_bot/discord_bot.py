# bot.py
import sys
import os
import discord

sys.path.append('../discord_bot')

from datetime import datetime
from create_images.skill_priority_image import create_skill_priority_image
from create_images.runes_image import create_rune_image
from create_images.starting_items_image import create_starting_items_image
from create_images.build_image import create_build_image
from create_images.final_image import build_final_image
from create_images.summoner_spells_image import create_summoner_spells_image
from create_embed import embed
from data_scrape.get_information import get_information

#TOKEN = os.getenv('DISCORD_TOKEN')
TOKEN = "OTI2OTAyOTA3MzEwMzIxNzU2.GWKn6K.yHOsE0Ga2wk6xsgM5q0l9Pm5IRufMXdIR7FcTc"

client = discord.Client()

"""
INPUT: User messages from a discord channel
OUTPUT: Outputs discord embeds for the champion build
DESCRIPTION: Recognizes messages starting with "8=D" and gets the recommended build of the champion requested in the message.
"""
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    command = message.content 
    # initial command
    if command.startswith('8=D'):
        try: 
            champion_and_role = command.split('8=D')[1].strip()
            champion_and_role = champion_and_role.split(" ")
            champion = champion_and_role[0]
            
            # role might not be specified
            role = ""
            try:
                role = champion_and_role[1]
                build = get_information(champion, role)
            except IndexError:
                build = get_information(champion)

            #First Embed - Title, Champion Thumbnail, Runes, Summoner Spells
            embedVar = embed(champion, role, build)

            runes = create_rune_image(build.runes)
            runes.save('runes.png')

            skill_priority = create_skill_priority_image(build.skill_priority)
            skill_priority.save('skill_priority.png')

            starting_items = create_starting_items_image(build.starting_items)
            starting_items.save("starting_items.png")

            final_build = create_build_image(build.build)
            final_build.save("final_build.png")

            summoners = create_summoner_spells_image(build.summoners)
            summoners.save("summoners.png")

            # combine all the images into one
            final_image = build_final_image(['runes.png', 'starting_items.png', 'build.png', 'summoners.png'])
            final_image.save('final_image.png')

            file = discord.File("final_image.png", filename = "final_image.png")
            embedVar.set_image(url = "attachment://final_image.png")
            
            print(f"start: {datetime.now()}")
            await message.channel.send(embed = embedVar, file = file)
            print(f"end: {datetime.now()}")
        except Exception as err:
            await message.channel.send(f"u dum dum do champ name and role, {err}")

if __name__ == "__main__":
    client.run(TOKEN)
