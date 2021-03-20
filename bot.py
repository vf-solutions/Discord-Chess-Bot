# invite link:
# https://discord.com/oauth2/authorize?client_id=721521983518670959&permissions=8&scope=bot

import discord
from discord.ext import commands
from discord.utils import get

import json
import ChessClient # for all of the Chess.com API data scrapping

import cairosvg
import ChessGame as chessgame # for the Discord-based Chess game

import os

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
            svg = request.board_to_svg()
            with open('board.svg', 'w') as f:
                f.write(svg)
                cairosvg.svg2png(url='board.svg', write_to='board.png')
                fi = discord.File('board.png')
                await ctx.send('Challenge from <@{0.id}> has been accepted!'.format(request.players[0]))
                await ctx.send('It is <@{0.id}>\'s turn!'.format(request.player), file=fi)
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
            valid, result = match.make_move(move)
            winner = None
            draw = False
            if result is not None:
                if result == '1-0':
                    winner = match.player
                elif result == '0-1':
                    winner = match.players[match.moves % 2]
                elif result == '1/2-1/2':
                    draw = True
            if not valid:
                await ctx.send('Invalid move, \'{0}\''.format(move))
            else:
                svg = match.board_to_svg()
                with open('board.svg', 'w') as f:
                    f.write(svg)
                    cairosvg.svg2png(url='board.svg', write_to='board.png')
                    fi = discord.File('board.png')
                    m = 'It is now <@{0.id}>\'s turn!'.format(match.player)
                    if winner is not None:
                        m = '<@{0.id}> wins!'.format(winner)
                    elif draw is True:
                        m = 'The match was a draw!'
                    await ctx.send(m, file=fi)
            if result is not None:
                matches.remove(match)
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

    embed = discord.Embed(title = "Kaweees's Player Stats", url = "https://google.com")
    embed.title = server.name
    embed.description = 'Server Info'
    embed.color = 0x7fa650
    embed.title = server.name
    await ctx.send(embed=embed)
    await ctx.send(":flag_us: :flag_US: ")

@client.command()
async def playerstats(ctx, username):
    try:
        playerGeneralData = ChessClientInstance.getPlayerInformation(username)
        print("Sucessfully fetched Data :D")
    except:
        channel = ctx.message.channel
        await channel.send('Invalid Chess.com username, please try again')
    
    embed = makeEmbed(playerGeneralData)
    await ctx.send(embed=embed) 

def getToken():
    # code to open and read token
    return os.environ.get('TOKEN')

def makeEmbed(playerStats):
    Chessplayer = ChessClient.Chessplayer(playerStats)
    playerStatsData = ChessClientInstance.getPlayerStats(Chessplayer.username)
    Chessplayer.updatePlayerStats(playerStatsData)
    embed = discord.Embed()
    embed.title = Chessplayer.embedname
    embed.url = Chessplayer.url
    embed.set_thumbnail(url=Chessplayer.avatarurl)
    embed.description = 'Player Info and Stats'
    embed.color = Chessplayer.color
    embed.add_field(name = "Country:", value = Chessplayer.getCountry(Chessplayer.country), inline = True)
    embed.add_field(name = "Date Joined:", value = f"{Chessplayer.dateJoined}", inline = True)
    embed.add_field(name = "Last Online:", value = f"{Chessplayer.lastOnline}", inline = True)
    embed.add_field(name = "<:bullet:816514940327297035> Bullet [x games played]", value = f"Rating: **x** - Highest Rating **{str(Chessplayer.chessBulletBest)}**", inline = False)
    embed.add_field(name = "<:blitz:816501491266355221> Blitz: [x games played]", value = f"Rating: **x** - Highest Rating **{str(Chessplayer.chessBlitzBest)}**", inline = False)
    embed.add_field(name = "<:rapid:816501511101087802> Rapid: [x games played]", value = f"Rating: **x** - Highest Rating **{str(Chessplayer.chessRapidBest)}**", inline = False)
    embed.add_field(name = "<:daily:816501455401648169> Daily: [x games played]", value = f"Rating: **x** - Highest Rating **{str(Chessplayer.chessDailyBest)}**", inline = False)
    return embed

ChessClientInstance = ChessClient.ChessClient()
client.run(getToken())