import discord
import asyncio
from discord.ext import commands
import random

description = '''THIS IS MUH BOT AND NOBODY FUCKS WITH MUH BOT'''
global infile

bot = commands.Bot(command_prefix=';', description=description)

@bot.event
async def on_ready():
    print('Logged in as ',end="")
    print(bot.user.name,end=" ")
    print(bot.user.id)
    print('------')
    #await bot.say("I'M READY\nI'M READY\nI'M READY")

@bot.command()
async def start():
    await bot.say('Starting a new madlib for you!')
    i = random.randint(1,100)
    if i > 0:
        infile = 




bot.run("MzM3ODA3ODY4Mjc3NDI0MTI4.DFgARg.js_CqztV4epoyPWaGZ_QfPue9v4")
