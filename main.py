import discord
from discord.ext import commands
import random
from topics import randomTopics

client = discord.Client()

TOKEN = "Your discord bot token / make this private if your using this code somewhere public"


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

    channel = client.get_channel("The channel you want to send the message to")
    await channel.send(random.choice(randomTopics) + " " + "@here")
    await client.close()


client.run(TOKEN)