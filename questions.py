
async def question(question, answer,  hint, client, message):

    score = 0

    await message.channel.send(question)

    response = await client.wait_for('message')

    if answer in response.content.lower():
        await message.channel.send("**\nBonne réponse !\n**")
        score = score + 2
        return score

    if "!indice" in response.content.lower():
        await message.channel.send(hint)

        response = await client.wait_for('message')

        if answer in response.content.lower():
            await message.channel.send("**\nBonne réponse !\n**")
            score = score + 1.5
            return score
        else:
            await message.channel.send("**\nDommage ce n'est pas la bonne réponse\n**")
            return score

    else:
        await message.channel.send("**\nDommage ce n'est pas la bonne réponse\n**")
        return score
