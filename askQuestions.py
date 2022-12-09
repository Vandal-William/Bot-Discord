from easyLvl import *


def askQuestions(client):

    @client.event
    async def on_message(message):  # fonction qui réagie a un message de l'utilisateur

        if message.content.lower() == "start":
            await message.channel.send("Voulez vous résoudre une énigme ?")

            response = await client.wait_for('message')

            if "oui" in response.content.lower():

                await message.channel.send("https://meilleurtest.fr/wp-content/uploads/2022/08/liste-mangas-shonen-du-moment-672x345.jpg")

                await message.channel.send("Bienvenu sur Mangas Quest ! Le but du jeu est de trouver le nom d'un manga a travers 5 question, des indices pour chaque question son disponible en tapant 'indice' et c'est partie pour le niveau facile !")

                await asyncio.sleep(15)

                await easyLvl(client, message)

            if "non" in response.content.lower():
                await message.channel.send("Dommage une prochaine fois peut etre")
