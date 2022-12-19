from enigma import *
from inspire import *
import asyncio


def runBot(client):

    @client.event
    async def on_message(message):  # fonction qui réagie a un message de l'utilisateur

        if message.content.lower() == "!start":

            username = str(message.author).split("#")[0]

            await message.channel.send("```\nBienvenu, " + username + " tapez !explain pour voir toutes les commandes du bot ou !ignore si vous les connaissez déja.\n```")

            response = await client.wait_for('message')

            if response.content.lower() == "!explain":
                 await message.channel.send("```\n--------------Mangas-quest-----------\n\n Voici les commandes du bot:\n\n -> !enigma pour résoudre une énigme\n -> !inspire pour une citation inspirrante\n\n Amusez vous bien sur Mangas-Quest ```")
             
            await asyncio.sleep(2)

            await message.channel.send("**\nQue souhaiter vous faire ?\n**")

            response = await client.wait_for('message')

            if response.content.lower() == "!enigma":

                await enigma(client, message)

            if response.content.lower() == "!inspire": 

                await askinspire(message, client)       