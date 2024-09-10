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
async def hello(ctx):
    await ctx.send("Hello, I am the test bot.")


@client.command()
async def goodbye(ctx):
    await ctx.send("This is the test for bot.")

@client.command()
async def studyTimer(ctx, minute, subject):
    minutes = int(minute)
    time_response = requests.get('https://timeapi.io/api/time/current/zone?timeZone=America%2FChicago')
    time_json = time_response.json()
    time_string = time_json['time'].split(':')
    curr_hour = int(time_string[0])
    curr_minute = int(time_string[1])
    if(curr_minute + minutes < 60):
        curr_minute = str(curr_minute+minutes)
        curr_hour = str(curr_hour)
    else:
        ex_hour = int(minutes/60)
        if((curr_minute+(int(minutes%60))) < 10):
            curr_minute = '0'+str((curr_minute+(int(minutes%60))))
        else:
            curr_minute = str((curr_minute+(int(minutes%60))))
        curr_hour = str(curr_hour + ex_hour)
    end_time = ':'.join([curr_hour, curr_minute])
    response = f"{ctx.author.name}'s study session:\n`{minutes} minutes`\n`Studying: {subject}`\n`Will be done at {end_time}`"
    await ctx.send(response)   
    curr_time = ''
    while(time_json['time'] != curr_time):
        time.sleep(60)
        time_response = requests.get('https://timeapi.io/api/time/current/zone?timeZone=America%2FChicago')
        time_json = time_response.json()
        curr_time = time_json['time']
    await ctx.send(f"{ctx.author.name}'s study session is done!")


    
client.run(BOTTOKEN)







