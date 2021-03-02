# invite link:
# https://discord.com/api/oauth2/authorize?client_id=744024313476415540&permissions=8&scope=bot

import discord
import json
print(discord._version)

client = discord.Client()

@client.event
async def on_ready(self):
    await client.change_presence(status=discord.Status.online, activity=discord.Game(name="Chess :D"))
    print("My body is ready")
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

def getToken():
    # code to open and read token
    with open('assts/token.txt', 'r') as file: # read file content
        data = file.read().replace('\n', '')
    return data # store file contents in data

client = discord.Client()
client.run(getToken())