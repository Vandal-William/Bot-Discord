import asyncio
from questions import *
import json

"""
Fonction qui se sert de la fonction questions pour poser les questions relatives au niveau de difficulté facile. 
Elle se sert également de la boucle for pour boucler sur le fichier easy.jison, pour poser des questions par itération. 
Elle push le score retourner par chaque question dans un tableau nommé totalScore. Enfin elle affiche le score final 
par la somme des valeurs présent dans le tableau
"""


async def runLvl(client, message, jsonfile, level):

    fileObject = open(jsonfile, "r")
    jsonContent = fileObject.read()
    q = json.loads(jsonContent)

    level = level
    totalScore = []

    for i in range(len(q)):

        Question = await question(q[i]["Question"], q[i]["Response"], q[i]["Hint"], client, message)

        await asyncio.sleep(2)

        totalScore.append(Question)

    await asyncio.sleep(2)

    await message.channel.send("**\nFélicitation vous avez terminer le niveau " + level + " avec un score de " + " " + str(sum(totalScore)) + "/" + str(10) + "\n**")
