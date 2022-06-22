# bot.py

import discord
from main import main
import os

TOKEN = os.getenv("DISCORD_TOKEN")


client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    command = message.content 
    # initial command
    if command.startswith('8=D'):
        champion = command.split('8=D')[1]
        build = main(champion)
        await message.channel.send("Your command STINKS!")
        await message.channel.send(build)
        

if __name__ == "__main__":
    client.run(TOKEN)
