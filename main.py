import discord
from discord.ext import commands
from discord.ext import tasks
import requests
import time
import datetime
from apikeys import *



client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@client.event
async def on_ready():
    print("The bot is now ready for use.")
    print("-----------------------------")

@client.command()
async def studyTimer(ctx, minute, subject):
    curr_time = datetime.datetime.now().strftime("%I:%M %p")
    end_time = datetime.datetime.fromtimestamp(time.time() + (int(minute)*60)).strftime("%I:%M %p")
    response = f"\n{ctx.author.name}'s Study Session:\n`{minute} Minutes`\n`Studying: {subject}`\n`End Time: {end_time}`"
    await ctx.send(response)




    
client.run(BOTTOKEN)







