# invite link:
# https://discord.com/api/oauth2/authorize?client_id=744024313476415540&permissions=8&scope=bot

import discord
from discord.ext import commands
from discord.utils import get
import json

intents = discord.Intents.all()
client = commands.Bot(command_prefix = '$', intents=intents)
client.remove_command("$help")

PREFIX = '$'

match_requests = [ ]
matches = [ ]

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game(name="Chess :D"))
    print("My body is ready")
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    await client.process_commands(message)
    global PREFIX
    global match_requests
    if message.content.startswith(PREFIX):
        command = message.content[1:]
        if command.startswith('hello'):
            await message.channel.send('Hello!')
        elif command.startswith('challenge'):
            await challenge(message.author, message.mentions[0])
            await message.channel.send('User {0.display_name}#{0.discriminator} has been challenged!'.format(message.mentions[0]))
        elif command.startswith('accept'):
            found = False
            for request in match_requests:
                # we have found the request
                if request['member'].id == message.author.id:
                    await message.channel.send('Challenge from <@{0.id}> has been accepted!'.format(request['challenger']))
                    matches.append(request)
                    match_requests.remove(request)
                    found = True
            if not found:
                await message.channel.send('No pending challenges!')

@client.command()
async def challenge(challenger: discord.Member, member: discord.Member):
    global match_requests

    # maybe convert to a class
    match_requests.append({
        'challenger': challenger, 'member': member
    })

@client.command()
async def server(ctx):
    """Shows server info"""
    channel = ctx.message.channel

    embed = discord.Embed(title=server.name, description='Server Info', color=0xEE8700)
    await ctx.send(embed=embed) 

def getToken():
    # code to open and read token
    with open('assets/token.txt', 'r') as file: # read file content
        data = file.read().replace('\n', '')
    return data # store file contents in data

client.run(getToken())