import discord
import os
from dotenv import load_dotenv
from runBot import *

intents = discord.Intents.all()
client = discord.Client(intents=intents)
global score
score = 0
load_dotenv()


@client.event
async def on_ready():
    print("le bot est prêt !")

runBot(client)

client.run(os.getenv('TOKEN'))
