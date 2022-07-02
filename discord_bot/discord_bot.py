# bot.py

import discord
import random
from datetime import datetime
from data_scrape.get_information import get_information
from create_images.runes_image import create_rune_image

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

            await message.channel.send(build.runes) #{'keystone': '', 'main_tree1': ''
            await message.channel.send(build.summoners) #[spell1, spell2]
            await message.channel.send(build.skills)    #['q','w','e',...]
            await message.channel.send(build.starting_items)
            await message.channel.send(build.build)

            #First Embed - Title, Champion Thumbnail, Runes, Summoner Spells

            embedVar = embed(champion, role, build)

            runes = create_rune_image(build.runes)
            runes.save('runes.png')
            file = discord.File('runes.png', filename = "runes.png")
            embedVar.set_image(url = "attachment://runes.png")
            print(f"start: {datetime.now()}")
            await message.channel.send(embed = embedVar, file = file)
            print(f"end: {datetime.now()}")
        except Exception as err:
            await message.channel.send(f"u dum dum do champ name and role, {err}")

"""
INPUT: Champion name, role, ResponseStruct object
OUTPUT: Outputs a single embed for runes and summoner spells
DESCRIPTION: Creates a discord embed for runes and summoner spells
"""
def embed(champion, role, build):
    championUpper = champion.capitalize()
    roleUpper = role.capitalize()

    embedVar = discord.Embed(
        title = championUpper + " " + roleUpper + " Build", 
        description = random.choice(POKEMON) + " whips out their huge throbbing cock, respectfully.",
        url = f"https://u.gg/lol/champions/{champion}/build?role={role}" if role != "" else f"https://u.gg/lol/champions/{champion}/build",
        color = discord.Color.blue(),
    )
    embedVar.set_thumbnail(url = f"https://static.u.gg/assets/lol/riot_static/12.12.1/img/champion/{championUpper}.webp")
    embedVar.add_field(name = "Skill Order", value = ''.join(build.skills), inline = "False")
    return embedVar

if __name__ == "__main__":
    client.run(TOKEN)
