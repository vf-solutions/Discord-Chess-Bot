# invite link:
# https://discord.com/api/oauth2/authorize?client_id=744024313476415540&permissions=8&scope=bot
import discord
from discord.ext import commands
from discord.utils import get
import json
from constants import *

token = "NzQ0MDI0MzEzNDc2NDE1NTQw.XzdMow.aa_S8fu3GCs6zayAr4EUHVZT0eU"
intents = discord.Intents.all()

client = commands.Bot(command_prefix = '$', intents=intents)
client.remove_command("$help")

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game(name="React to my messages in #select-roles to show others the classes you are in"))
    # with open('assets/img/fox.jpg', 'rb') as f:
    #     await client.edit_profile(avatar=f.read())
    print("My body is ready")

@client.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    if payload.user_id != 744024313476415540: #checks if reaction is from bot
        print("Add role initiated")
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)
        value = payload.emoji.name
        # print(value) used in debugging
        global all_roles_list
        for i in range(len(all_roles_list)):
            if all_roles_list[i] in value:
                role = discord.utils.get(guild.roles, name=all_roles_dict[all_roles_list[i]])
                print(role)
                break
        if role is None:
            print("Role not found")
            await guild.create_role(name=all_roles_dict[all_roles_list[i]], mentionable=True)
            for i in range(len(all_roles_list)):
                if all_roles_list[i] in value:
                    role = discord.utils.get(guild.roles, name=all_roles_dict[all_roles_list[i]])
                    print(role)
                    break
        member = payload.member
        if member:
            await role.edit(mentionable=True)
            await member.add_roles(role)
            print("success")
        else:
            print("Member not found")
    else:
        print("The bot reacted")
        print(payload.user_id)

@client.event
async def on_raw_reaction_remove(payload):
    message_id = payload.message_id
    if payload.user_id != 744024313476415540: #checks if reaction is from bot
        print("Add role initiated")
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)
        value = payload.emoji.name
        # print(value) used in debugging
        global all_roles_list
        for i in range(len(all_roles_list)):
            if all_roles_list[i] in value:
                role = discord.utils.get(guild.roles, name=all_roles_dict[all_roles_list[i]])
                print(role)
                break
        if role is None:
            print("Role not found")
            await guild.create_role(name=all_roles_dict[all_roles_list[i]], mentionable=True)
            for i in range(len(all_roles_list)):
                if all_roles_list[i] in value:
                    role = discord.utils.get(guild.roles, name=all_roles_dict[all_roles_list[i]])
                    print(role)
                    break
        member = get(guild.members, id=payload.user_id)
        if member:
            await role.edit(mentionable=True)
            await member.remove_roles(role)
            print("success")
        else:
            print("Member not found")
    else:
        print("The bot reacted")
        print(payload.user_id)

# Loads the Config.json File so stuff can be easilly Changed instead of having to return to the code every time
with open('./config.json') as f:
    config = json.load(f)
n_channel_id = int(config['names-channel-id'])

@client.event
async def on_message(message):
    if message.content.lower().find("hello there") != -1:
        await message.channel.send("General Kenobi") # If the user says !hello we will send back hi
    elif message.content.lower().find("i don't like sand") != -1:
        channel = message.channel
        await message.add_reaction("🏖️")
        await message.add_reaction("⏳")
        await message.add_reaction("🏜️")
        filename = "assets/img/sand.jpg"
        await channel.send(file=discord.File(filename))
        print(f"File '{filename}' was sent on {message.channel}")
    # If the Message was sent to The Names Channel Specified in the config.json then the user's Nickname is Changed to it.
    # TODO: Also Assigns Specified Role in Config.json
    elif message.channel.id == n_channel_id:
        await message.author.edit(nick=message.content)
    await client.process_commands(message)
    if (message.author.bot) and (message.author.id == client.user.id): #checks if message is from bot
        global all_roles_list
        print(message.embeds)
        for embed in (message.embeds):
            for field in embed.fields:
                # print(field.name)
                print(field.value)
                value = field.value
                for i in range(len(all_roles_list)):
                    if all_roles_list[i] in value:
                        await message.add_reaction(all_roles_list[i])
    else:
        print(message.author.name)

@client.event
async def on_member_join(member):
    guild = member.guild
    print(guild)
    rules = guild.get_channel(633477240797134870)
    pick_roles = guild.get_channel(745093331318734989)
    names = guild.get_channel(633490755889135626)
    channel = guild.get_channel(633473337766576139)
    await channel.send(f'Welcome {member.mention}! Make sure to check {rules.mention} for server rules and {pick_roles.mention} for class roles. Also change your nickname to your irl name in {names.mention}.')

@client.command()
async def setroles(ctx):
    channel = ctx.message.channel
    if ctx.message.author.guild_permissions.administrator:
        async for message in channel.history(limit=200): # clears all of the bot messages in the channel
            if message.author == client.user:
                await message.delete()
        await ctx.message.delete()
        global special_roles
        # TODO remove previous messages the bot sent in the channel
        for key in special_roles.keys():
            embed=discord.Embed(color=0xFF0000)
            embed.add_field(name=f"Role Menu: {key}", value="React to give yourself a role.", inline=False)
            for subkeys in special_roles[key].keys():
                embed.add_field(name="\u200b", value=f'{subkeys} : {special_roles[key][subkeys]}', inline=False)
            await ctx.send(embed=embed)
    else:
        msg = f"Sorry {ctx.message.author.mention}, only Admins can use this command"
        await channel.send(msg)

@client.command()
async def test(ctx, *, arg):
    print(arg)
    await ctx.send(arg)


@client.command()
async def ping(ctx):
    print(ctx)
    await ctx.send(f'Pong! {round(client.latency * 1000)} ms')

client.run(token)
"""@client.command(name="help", description="Returns all commands available")
async def help(ctx):
    helptext = "```"
    for command in self.bot.commands:
        helptext+=f"{command}\n"
    helptext+="```"
    await ctx.send(helptext)
@client.command(pass_context=True)
async def profile(ctx):
    await ctx.message.delete()
    embed=discord.Embed(color=0xFF0000)
    embed.add_field(icon_url=ctx.author.avatar_url, text=f"{ctx.author.name}#{ctx.author.discriminator}")
    embed.add_field(name='Classes', text=f"AP Bio", inline=True)
    embed.add_field(name='Scammer', value='$lookup, $int', inline=True)
    embed.add_field(name='Other', value='$bitcoin, $info', inline=False)
    await ctx.send(embed=embed)
"""
# "⚙️" : "AP Physics C: Mechanics",
# "🧲" : "AP Physics C: Electricity and Magnetism"
# "🧪" : "AP Chemistry",
# "🌲" : "AP English Literature and Composition"
# "🆎" : "AP Calculus BC",
# "📜" : "AP US Government and Politics",
# "🌐" : "AP World History: Modern",
# "📉" : "AP Microeconomics",
# "📈" : "AP Macroeconomics",
# "🔩" : "Engineering Design and Development (EDD)"
# "💉" : "Intermediate Biotechnology 3",
