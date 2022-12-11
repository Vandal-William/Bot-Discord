from runLvl import *
import asyncio


async def enigma(client, message):

    await message.channel.send("https://meilleurtest.fr/wp-content/uploads/2022/08/liste-mangas-shonen-du-moment-672x345.jpg")

    await message.channel.send("```\nBienvenu sur enigma de Mangas Quest ! Le but du jeu est de trouver le nom d'un manga a travers 5 question, des indices pour chaque question son disponible en tapant '!indice'\n```")
    
    await asyncio.sleep(2)

    await message.channel.send("**\nNiveau facile\n**")

    await asyncio.sleep(2)

    level_easy = await runLvl(client, message, "./easy_level/easy.json", "Facile")
    
    if level_easy == 1:
        await runLvl(client, message, "./easy_level/easy.json", "Facile")
    if level_easy == 0:
        await message.channel.send("**\nDommage une prochaine fois peut etre\n**")
        return

    await asyncio.sleep(2)

    await message.channel.send("**\nVous avez terminer le niveau facile, prèt pour le niveau normal ?\n -> !oui pour continuer\n -> !non pour quitter\n**")

    response = await client.wait_for('message')

    if response.content.lower() == "!oui":
        await asyncio.sleep(2)

        await message.channel.send("**\nNiveau normal\n**")
        
        await asyncio.sleep(2)

        level_normal = await runLvl(client, message, "./normal_level/normal.json", "Normal")

        if level_normal == 1:
            await runLvl(client, message, "./normal_level/normal.json", "Normal")
        if level_normal == 0:
            await message.channel.send("**\nDommage une prochaine fois peut etre\n**")
            return

    if response.content.lower() == "!non":
        await asyncio.sleep(2)
        await message.channel.send("**\nDommage une prochaine fois peut etre\n**")
        return

    await asyncio.sleep(2)
    await message.channel.send("**\nVous avez terminer le niveau normal, prèt pour le niveau difficile ?\n -> !oui pour continuer\n -> !non pour quitter\n**")

    response = await client.wait_for('message')

    if response.content.lower() == "!oui":

        await asyncio.sleep(2)

        await message.channel.send("**\nNiveau difficile\n**")

        await asyncio.sleep(2)

        level_difficult = await runLvl(client, message, "./difficult_level/difficult.json", "Difficile")

        if level_difficult == 1:
            await runLvl(client, message, "./difficult_level/difficult.json", "Difficile")
        if level_difficult == 0:
            await message.channel.send("**\nDommage une prochaine fois peut etre\n**")
            return

        if level_difficult == 2:

            await asyncio.sleep(2)

            await message.channel.send("**\n Il n'y a plus d'énigme a résoudre, félicitation ! \n**")

            await asyncio.sleep(2)

            await message.channel.send("**\n Voulez vous refaire une partie ?\n -> !oui pour continuer\n -> !non pour quitter\n**")

            response = await client.wait_for('message')

            if response.content.lower() == "!oui": 
                await enigma(client, message)
            if response.content.lower() == "!non":
                await message.channel.send("**\n trés bien, tapez !start pour redémarrer le bot \n**") 
                return   

    if response.content.lower() == "!non" :
        await asyncio.sleep(2)
        await message.channel.send("\n**Dommage une prochaine fois peut etre\n**")
        return

   
