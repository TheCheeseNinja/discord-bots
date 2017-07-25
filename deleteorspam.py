##Delete msgs bot
import asyncio
import discord
from discord.ext import commands

#spam msgs
bot = commands.Bot(command_prefix='$', description='test')

@bot.event
async def on_ready():
    print('ready to spam sir')

@bot.command()
async def spam():
    while True:
        await bot.say("and they don't stop coming")

bot.run('MzM5MjYwODc4NjEwNDk3NTM3.DFhY5Q.-dUEby-eF9SNUkf1ujILSD4cOxw')


####1st option: try next
####
####Client = Bot('!')
####
####@Client.command(pass_context = True)
####async def clear(ctx, number):
####    number = int(number) #Converting the amount of messages to delete to an integer
####    counter = 0
####    async for x in Client.logs_from(ctx.message.channel, limit = number):
####        if counter < number:
####            await Client.delete_message(x)
####            counter += 1
####            await asyncio.sleep(1.2) #1.2 second timer so the deleting process can be even
####
####Client.run(Token)



#2nd option (prob best)
######
######client = discord.Client()
######
######@client.event
######async def on_message(message):
######    if message.content.startswith('!clear'):
######        tmp = await client.send_message(message.channel, 'Clearing messages...')
######        async for msg in client.logs_from(message.channel):
######            await client.delete_message(msg)
######            
######
######client.run('MzM5MjYwODc4NjEwNDk3NTM3.DFhY5Q.-dUEby-eF9SNUkf1ujILSD4cOxw')
