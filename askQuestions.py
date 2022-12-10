from enigma import *
import asyncio

"""
Fonction qui dans un premier temps, présente le jeu à l'utilisateur et qui lance les niveaux de difficulté.
"""


def askQuestions(client):

    @client.event
    async def on_message(message):  # fonction qui réagie a un message de l'utilisateur

        if message.content.lower() == "start":

            username = str(message.author).split("#")[0]

            await message.channel.send("```\nBienvenu, " + username + "\n```")

            await asyncio.sleep(2)

            await message.channel.send("**\nQue souhaiter vous faire ?\n**")

            response = await client.wait_for('message')

            if response.content.lower() == "!quizz":

                await enigma(client, message)
