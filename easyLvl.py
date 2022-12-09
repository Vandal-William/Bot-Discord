import asyncio
from questions import *
import json


async def easyLvl(client, message):

    fileObject = open("easy.json", "r")
    jsonContent = fileObject.read()
    q = json.loads(jsonContent)

    level = 'facile'

    questionA = await question(q[0]["Question1"], q[0]["Response1"], q[0]["Hint1"], client, message)

    await asyncio.sleep(2)

    questionB = await question(q[1]["Question2"], q[1]["Response2"], q[1]["Hint2"], client, message)

    await asyncio.sleep(2)

    questionC = await question(q[2]["Question3"], q[2]["Response3"], q[2]["Hint3"], client, message)

    await asyncio.sleep(2)

    questionD = await question(q[3]["Question4"], q[3]["Response4"], q[3]["Hint4"], client, message)

    await asyncio.sleep(2)

    questionE = await question(q[4]["Question5"], q[4]["Response5"], q[4]["Hint5"], client, message)

    await asyncio.sleep(2)

    await message.channel.send("Félicitation vous avez terminer le niveau " + level + " avec un score de " + " " + str(float(questionA) + float(questionB) + float(questionC) + float(questionD) + float(questionE)) + "/" + str(10))
