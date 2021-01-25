import discord
import grass
import const

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    
    if message.content.startswith('$test'):
        grass.printTest()
        await message.channel.send('testttttttttt!')

client.run(const.TOKEN)
