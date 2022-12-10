from easyLvl import *
from normalLvl import *
from difficultLvl import *


"""
Fonction qui dans un premier temps, présente le jeu à l'utilisateur et qui lance les niveaux de difficulté.
"""


def askQuestions(client):

    @client.event
    async def on_message(message):  # fonction qui réagie a un message de l'utilisateur

        if message.content.lower() == "start":
            await message.channel.send("**\nVoulez vous résoudre une énigme ?\n**")

            response = await client.wait_for('message')

            if "oui" in response.content.lower():

                await message.channel.send("https://meilleurtest.fr/wp-content/uploads/2022/08/liste-mangas-shonen-du-moment-672x345.jpg")

                await message.channel.send("```Bienvenu sur Mangas Quest ! Le but du jeu est de trouver le nom d'un manga a travers 5 question, des indices pour chaque question son disponible en tapant 'indice' et c'est partie pour le niveau facile !\n\n```")

                await asyncio.sleep(5)

                await easyLvl(client, message)

                await asyncio.sleep(2)

                await message.channel.send("**\nVous avez terminer le niveau facile, prèt pour le niveau normal ?\n**")

                response = await client.wait_for('message')

                if "oui" in response.content.lower():
                    await asyncio.sleep(2)
                    await normalLvl(client, message)

                if "non" in response.content.lower():
                    await asyncio.sleep(2)
                    await message.channel.send("**\nDommage une prochaine fois peut etre\n**")

                await asyncio.sleep(2)
                await message.channel.send("**\nVous avez terminer le niveau normal, prèt pour le niveau difficile ?\n**")

                response = await client.wait_for('message')

                if "oui" in response.content.lower():
                    await asyncio.sleep(2)
                    await difficultLvl(client, message)

                if "non" in response.content.lower():
                    await asyncio.sleep(2)
                    await message.channel.send("\n**Dommage une prochaine fois peut etre\n**")

            if "non" in response.content.lower():
                await asyncio.sleep(2)
                await message.channel.send("**\nDommage une prochaine fois peut etre\n**")
