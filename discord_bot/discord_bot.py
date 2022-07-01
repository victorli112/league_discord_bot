# bot.py

import discord
import random
from data_scrape.get_information import get_information
import os
from PIL import Image
import requests
import base64
import io
from io import BytesIO

#TOKEN = os.getenv('DISCORD_TOKEN')
TOKEN = "OTI2OTAyOTA3MzEwMzIxNzU2.GWKn6K.yHOsE0Ga2wk6xsgM5q0l9Pm5IRufMXdIR7FcTc"

POKEMON = ["Bulbasaur","Ivysaur","Venusaur","Charmander","Charmeleon","Charizard","Squirtle","Wartortle","Blastoise","Caterpie","Metapod","Butterfree","Weedle","Kakuna","Beedrill","Pidgey","Pidgeotto","Pidgeot","Rattata","Raticate","Spearow","Fearow","Ekans","Arbok","Pikachu","Raichu","Sandshrew","Sandslash","Nidoran","Nidorina","Nidoqueen","Nidoran","Nidorino","Nidoking","Clefairy","Clefable","Vulpix","Ninetales","Jigglypuff","Wigglytuff","Zubat","Golbat","Oddish","Gloom","Vileplume","Paras","Parasect","Venonat","Venomoth","Diglett","Dugtrio","Meowth","Persian","Psyduck","Golduck","Mankey","Primeape","Growlithe","Arcanine","Poliwag","Poliwhirl","Poliwrath","Abra","Kadabra","Alakazam","Machop","Machoke","Machamp","Bellsprout","Weepinbell","Victreebel","Tentacool","Tentacruel","Geodude","Graveler","Golem","Ponyta","Rapidash","Slowpoke","Slowbro","Magnemite","Magneton","Farfetch'd","Doduo","Dodrio","Seel","Dewgong","Grimer","Muk","Shellder","Cloyster","Gastly","Haunter","Gengar","Onix","Drowzee","Hypno","Krabby","Kingler","Voltorb","Electrode","Exeggcute","Exeggutor","Cubone","Marowak","Hitmonlee","Hitmonchan","Lickitung","Koffing","Weezing","Rhyhorn","Rhydon","Chansey","Tangela","Kangaskhan","Horsea","Seadra","Goldeen","Seaking","Staryu","Starmie","Mr. Mime","Scyther","Jynx","Electabuzz","Magmar","Pinsir","Tauros","Magikarp","Gyarados","Lapras","Ditto","Eevee","Vaporeon","Jolteon","Flareon","Porygon","Omanyte","Omastar","Kabuto","Kabutops","Aerodactyl","Snorlax","Articuno","Zapdos","Moltres","Dratini","Dragonair","Dragonite","Mewtwo","Mew"]
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
            embedVar = await embed(champion, role, build)

            runes = await championSelectBuild(build.runes)
            runes.save('runes.png')
            file = discord.File('runes.png', filename = "runes.png")
            embed.set_image(url = "attachment://runes.png")

            await message.channel.send(embed = embedVar, file = file)
            #Second Embed - Skills, Starting Items, Runes
        except Exception as err:
            await message.channel.send(f"u dum dum do champ name and role, {err}")

"""
INPUT: Champion name, role, ResponseStruct object
OUTPUT: Outputs a single embed for runes and summoner spells
DESCRIPTION: Creates a discord embed for runes and summoner spells
"""
async def embed(champion, role, build):
    championUpper = champion.capitalize()
    roleUpper = role.capitalize()

    embedVar = discord.Embed(
        title = championUpper + " " + roleUpper + " Build", 
        description = random.choice(POKEMON) + " whips out their huge throbbing cock, respectfully.",
        url = f"https://u.gg/lol/champions/{champion}/build?role={role}" if role != "" else f"https://u.gg/lol/champions/{champion}/build",
        color = discord.Color.blue(),
    )
    embedVar.set_thumbnail(url = f"https://static.u.gg/assets/lol/riot_static/12.12.1/img/champion/{championUpper}.webp")
    # embedVar.set_image(url = await championSelectBuild(build.runes))
    await championSelectBuild(build.runes)
    return embedVar

"""
INPUT: Runes dictionary from ResponseStruct object
OUTPUT: URL of combined image of all the rune urls from the dict
DESCRIPTION: Converts urls to images with BytesIO. Combine images with Pillow. Combined image used for embed.
"""
async def championSelectBuild(runes):
    #Convert image urls to readable image files
    response = requests.get(runes['keystone'])
    img1 = Image.open(BytesIO(response.content))
    response = requests.get(runes['main_tree1'])
    img2 = Image.open(BytesIO(response.content))
    #Combine shit. Runes 64 x 64. Shards 32 x 32
    big = Image.new('RGB', ((img1.width + img2.width), img1.height))
    big.paste(img1, (0,0))
    big.paste(img2, (img1.width, 0))
    return big

if __name__ == "__main__":
    client.run(TOKEN)
