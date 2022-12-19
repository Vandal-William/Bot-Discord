import asyncio
from questions import *
import json

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


    if sum(totalScore) < 5:
        await message.channel.send("**\n Votre score est de :"+ " " + str(sum(totalScore)) + "/" + str(10) + ", il faut avoir un score minimum de 5/10 pour passer au niveau suivant.\n voulez vous rejouer ce niveau ?\n -> !oui pour continuer\n -> !non pour quitter\n**")
        response = await client.wait_for('message')
        if response.content.lower() == "!oui":
            return 1
        if response.content.lower() == "!non":
            return 0                
    else:
        await message.channel.send("**\nFélicitation vous avez terminer le niveau " + level + " avec un score de " + " " + str(sum(totalScore)) + "/" + str(10) + "\n**")
        return 2
    
