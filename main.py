import discord
from discord.ext import commands
import datetime

TOKEN = ''

intents = discord.Intents.default()
intents.members = True

class Server_Data:
    def __init__(self,id):
        self.id = id
        self.whitelist = []
        self.mindate = None




server_list = []

client = commands.Bot(command_prefix='*', intents=intents)


@client.event
async def on_ready():
    print('Logged in as', str(client))
    for server in client.guilds:
        server_data = Server_Data(server.id)
        server_list.append(server_data)
    print(server_list)

@client.event
async def on_guild_join(guild):
    server = Server_Data(guild.id)
    server_list.append(server)
    print(server_list)

@client.event
async def on_guild_remove(guild):
    for server in server_list:
        if server.id == guild.id:
            server_list.remove(server)
            break


@client.command()
async def kickafter(ctx, date=None):

    if not date:
        date = datetime.datetime.now() - datetime.timedelta(14)
    else:
        try:
            date = datetime.datetime.strptime(date, '%d/%m/%Y')
        except Exception:
            await ctx.send("Invalid date format! The format must be dd/mm/yyyy!")
            return
    server_data = ''
    members = ctx.guild.members
    for server in server_list:
        if server.id == ctx.guild.id:
            server_data = server
    for member in members:
        if member.created_at > date and member != client.user and member not in server_data.whitelist:
            try:
                await member.kick(reason=None)
            except Exception:
                await ctx.send("Couldn't kick member " + str(member))


@client.command()
async def banafter(ctx, date=None):
    if not date:
        date = datetime.datetime.now() - datetime.timedelta(14)
    else:
        try:
            date = datetime.datetime.strptime(date, '%d/%m/%Y')
        except Exception:
            await ctx.send("Invalid date format! The format must be dd/mm/yyyy!")
            return
    server_data = ''
    members = ctx.guild.members
    for server in server_list:
        if server.id == ctx.guild.id:
            server_data = server
            break
    for member in members:
        if member.created_at > date and member != client.user and member not in server_data.whitelist:
            try:
                await member.kick(reason=None)
            except Exception:
                await ctx.send("Couldn't kick member " + str(member))


@client.event
async def on_member_join(member):
    server_data = ''
    for server in server_list:
        if server.id == member.guild.id:
            server_data = server
    if not server_data.mindate:
        return
    if member.created_at > server_data.mindate and member != client.user:
        await member.kick(reason='Account too young!')


@client.command()
async def whitelist(ctx, member: discord.Member = None):
    server_data = ''
    for server in server_list:
        if server.id == ctx.guild.id:
            server_data = server
            break
    if not member:
        members = ctx.guild.members
        for member in members:
            server_data.whitelist.append(member)
    elif member in ctx.guild.members:
        server_data.whitelist.append(member)


@client.command()
async def setmindate(ctx, date=None,):
    if not date:
        return
    try:
        date = datetime.datetime.strptime(date, '%d/%m/%Y')
        server_data = ''
        for server in server_list:
            if server.id == ctx.guild.id:
                server_data = server
        server_data.mindate = date
    except Exception:
        await ctx.send("Invalid date format! The format must be dd/mm/yyyy!")
        return

@client.command()
async def getmindate(ctx):
    for server in server_list:
        if server.id == ctx.guild.id:
            await ctx.send(str(server.mindate))
            break


client.run(TOKEN)
