# bot.py

import discord
from main import main

TOKEN = 'OTI2OTAyOTA3MzEwMzIxNzU2.GOTCAQ.ecOS_RvD5GfqCQs8cNkLbT7cQnQ7O2jUf9-kEE'


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
        


client.run(TOKEN)
