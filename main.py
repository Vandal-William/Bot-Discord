import discord
import os
from dotenv import load_dotenv
from askQuestions import *


# Création d'une instance pour connecter le bot au serveur discord
intents = discord.Intents.all()
client = discord.Client(intents=intents)
score = 0
load_dotenv()


@client.event  # Déclarateur d'évènement
async def on_ready():  # cette fonction indique que le bot est prêt a exécuter des commandes
    print("le bot est prêt !")

askQuestions(client)

# Démarrage du serveur avec le  token
client.run(os.getenv('TOKEN'))
