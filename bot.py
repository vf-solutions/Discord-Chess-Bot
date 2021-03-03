# invite link:
# https://discord.com/api/oauth2/authorize?client_id=744024313476415540&permissions=8&scope=bot

import discord
from discord.ext import commands
from discord.utils import get
import json

import cairosvg

import ChessClient # for all of the Chess.com API data scrapping
import ChessGame as chessgame

intents = discord.Intents.all()
client = commands.Bot(command_prefix = '$', intents=intents)
client.remove_command("$help")

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

@client.command()
async def challenge(ctx: discord.ext.commands.Context):
    """Challenges user to a match"""
    global match_requests
    message = ctx.message

    challenger = message.author
    member = message.mentions[0]

    match_requests.append(chessgame.ChessGame(challenger, member))
    await ctx.send('User {0.display_name}#{0.discriminator} has been challenged!'.format(message.mentions[0]))

@client.command()
async def accept(ctx: discord.ext.commands.Context):
    """Accepts a user's request"""
    global match_requests
    global matches
    message = ctx.message

    found = False
    for request in match_requests:
        # we have found the request
        if request.players[1].id == message.author.id:
            await ctx.send('Challenge from <@{0.id}> has been accepted!'.format(request.players[0]))
            matches.append(request)
            match_requests.remove(request)
            found = True
    if not found:
        await ctx.send('No pending challenges!')

@client.command()
async def move(ctx: discord.ext.commands.Context):
    """Makes move"""
    global matches

    message = ctx.message
    move = message.content.split(' ')[1]

    found = False
    for match in matches:
        # we have found the match
        if match.player.id == message.author.id:
            found = True
            if not match.make_move(move):
                await ctx.send('Invalid move, \'{0}\''.format(move))
            else:
                svg = match.board_to_svg()
                with open('board.svg', 'w') as f:
                    f.write(svg)
                    cairosvg.svg2png(url='board.svg', write_to='board.png')
                    fi = discord.File('board.png')
                    await ctx.send(file=fi)
    if not found:
        await ctx.send('No match currently.')

@client.command()
async def end(ctx: discord.ext.commands.Context):
    """Ends match, what a loser"""
    global matches

    message = ctx.message

    found = False
    for match in matches:
        # we have found the match
        if match.player.id == message.author.id:
            found = True
            matches.remove(match)
            await ctx.send('Match forfeited.')
    if not found:
        await ctx.send('No match currently.')

@client.command()
async def server(ctx):
    """Shows server info"""
    channel = ctx.message.channel

    embed = discord.Embed(title = "Kaweees's Player Stats", url = "url goes here")
    embed.title = server.name
    embed.description = 'Server Info'
    embed.color = 0x7fa650
    embed.title = server.name
    await ctx.send(embed=embed) 

@client.command()
async def playerstats(ctx, username):
    try:
        data = ChessClientInstance.getPlayerInformation(username)
        print(data)
    except:
        channel = ctx.message.channel
        await channel.send('Invalid Chess.com username, please try again')
    embed = makeEmbed(data)
    await ctx.send(embed=embed) 

def getToken():
    # code to open and read token
    with open('assets/token.txt', 'r') as file: # read file content
        data = file.read().replace('\n', '')
    return data # store file contents in data

def makeEmbed(playerStats):
    Chessplayer = ChessClient.Chessplayer(playerStats)
    embed = discord.Embed()
    embed.title = Chessplayer.embedname
    embed.url = Chessplayer.url
    print(Chessplayer.avatarurl, "url boiii")
    embed.set_thumbnail(url=Chessplayer.avatarurl)
    embed.description = 'Server Info'
    embed.color = Chessplayer.color
    return embed

ChessClientInstance = ChessClient.ChessClient()
client.run(getToken())