# bot.py

import discord
import random
from data_scrape.get_information import get_information
import os

TOKEN = os.getenv('DISCORD_TOKEN')

POKEMON = ["Bulbasaur","Ivysaur","Venusaur","Charmander","Charmeleon","Charizard","Squirtle","Wartortle","Blastoise","Caterpie","Metapod","Butterfree","Weedle","Kakuna","Beedrill","Pidgey","Pidgeotto","Pidgeot","Rattata","Raticate","Spearow","Fearow","Ekans","Arbok","Pikachu","Raichu","Sandshrew","Sandslash","Nidoran","Nidorina","Nidoqueen","Nidoran","Nidorino","Nidoking","Clefairy","Clefable","Vulpix","Ninetales","Jigglypuff","Wigglytuff","Zubat","Golbat","Oddish","Gloom","Vileplume","Paras","Parasect","Venonat","Venomoth","Diglett","Dugtrio","Meowth","Persian","Psyduck","Golduck","Mankey","Primeape","Growlithe","Arcanine","Poliwag","Poliwhirl","Poliwrath","Abra","Kadabra","Alakazam","Machop","Machoke","Machamp","Bellsprout","Weepinbell","Victreebel","Tentacool","Tentacruel","Geodude","Graveler","Golem","Ponyta","Rapidash","Slowpoke","Slowbro","Magnemite","Magneton","Farfetch'd","Doduo","Dodrio","Seel","Dewgong","Grimer","Muk","Shellder","Cloyster","Gastly","Haunter","Gengar","Onix","Drowzee","Hypno","Krabby","Kingler","Voltorb","Electrode","Exeggcute","Exeggutor","Cubone","Marowak","Hitmonlee","Hitmonchan","Lickitung","Koffing","Weezing","Rhyhorn","Rhydon","Chansey","Tangela","Kangaskhan","Horsea","Seadra","Goldeen","Seaking","Staryu","Starmie","Mr. Mime","Scyther","Jynx","Electabuzz","Magmar","Pinsir","Tauros","Magikarp","Gyarados","Lapras","Ditto","Eevee","Vaporeon","Jolteon","Flareon","Porygon","Omanyte","Omastar","Kabuto","Kabutops","Aerodactyl","Snorlax","Articuno","Zapdos","Moltres","Dratini","Dragonair","Dragonite","Mewtwo","Mew"]
client = discord.Client()

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
            try:
                role = champion_and_role[1]
                build = get_information(champion, role)
            except IndexError:
                build = get_information(champion)
            await message.channel.send(random.choice(POKEMON))
            await message.channel.send(build)
        except Exception as err:
            await message.channel.send(f"u dum dum do champ name and role, {err}")

async def embed(champion, role):
    championUpper = champion.capitalize()
    roleUpper = role.capitalize()
    embedVar = discord.Embed(
        title= championUpper + " " + roleUpper + " Build", 
        #description = random.choice(POKEMON) + " whips out their huge throbbing cock, respectfully.",
        url = f"https://u.gg/lol/champions/{champion}/build?role={role}",
        color=discord.Color.blue(),
    )
    embedVar.set_thumbnail(url = f"https://static.u.gg/assets/lol/riot_static/12.12.1/img/champion/{championUpper}.webp")
    return embedVar
    
if __name__ == "__main__":
    client.run(TOKEN)
