import discord
import asyncio
from discord.ext.commands import Bot

##my_bot = Bot(command_prefix="!")
##@my_bot.event
##async def on_read():
##    print("Client logged in")
##@my_bot.command()
##async def hello(*args):
##    return await my_bot.say("Hello, world!")
##@my_bot.command()
##async def test():
##    my_bot.say('testing shit now')
##    a = 2+1
##    #my_bot.say(a)
##    #async def test():
##        #return await my_bot.say('test')
##    return await my_bot.say(a)
##my_bot.run("MzM3ODA3ODY4Mjc3NDI0MTI4.DFgARg.js_CqztV4epoyPWaGZ_QfPue9v4")

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')

@client.event
async def get_madlib(message):
    #lowered = message.content.lower()
    if message.content.lower().startswith(';start'):
        tmp = await client.send_message(message.channel, 'calculating...')
        await client.edit_message(tmp, 'get that madlib')
        await client.send_message(message.channel)

client.run('MzM3ODA3ODY4Mjc3NDI0MTI4.DFgARg.js_CqztV4epoyPWaGZ_QfPue9v4')
