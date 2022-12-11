import json
import random
import asyncio

async def askinspire(message, client):
    fileObject = open("inspire.json", "r")
    jsonContent = fileObject.read()
    ins = json.loads(jsonContent)
    
    i = random.randint(0, len(ins))
    await message.channel.send(ins[i]["inspire"])
    await message.channel.send(ins[i]["image"])
    await asyncio.sleep(2)

    await message.channel.send("```\nTapez !start pour relancer le bot ou !inspire pour une autre citation\n```")
    response = await client.wait_for('message')
    if response.content.lower() == "!inspire":
        await askinspire(message, client)