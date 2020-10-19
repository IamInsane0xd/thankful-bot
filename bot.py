import discord
import os
import time
import nacl
from discord.ext import commands, tasks
from discord.utils import get
from itertools import cycle

client = commands.Bot(command_prefix = 't.')
client.remove_command('help')
status = cycle(['t. | official thankful bot',
                't. | created by IamInsane#0001',
                "t. | ť̴̐r̵̍͠ä̵̍͑p̴̈́͝#7677 is gay"])

@client.event
async def on_ready():
    try:
        status_change.start()
    except:
        print("Task 'status_change' already running")
        print('')

    print('')
    print('canada mode activated')
    print('(bot is ready)')
    print('')

@tasks.loop(seconds = 15)
async def status_change():
    await client.change_presence(activity = discord.Game(next(status)))

@client.command()
async def load(ctx, extension):
    if ctx.message.author.guild_permissions.administrator:
        client.load_extension('cogs.{}'.format(extension))
        await ctx.send('Extension *{}* loaded succesfuly!'.format(extension))
    else:
        await ctx.send('Sorry, {}, you dont have permissions...'.format(ctx.message.author))

@client.command()
async def unload(ctx, extension):
    if ctx.message.author.guild_permissions.administrator:
        client.unload_extension('cogs.{}'.format(extension))
        await ctx.send('Extension *{}* unloaded succesfuly!'.format(extension))
    else:
        await ctx.send('Sorry, {}, you dont have permissions...'.format(ctx.message.author))

@client.command()
async def extlist(ctx):
    if ctx.message.author.guild_permissions.administrator:
        prefix = "t."

        embed = discord.Embed(title = 'Extension List', description = 'All the extensions the bot has:', colour = 0xFF3D67)

        embed.add_field(name = '_8ball', value = '({}8ball)'.format(prefix), inline = True)
        embed.add_field(name = 'clr', value = '({0}clear / purge, {0}nuke)'.format(prefix), inline = True)
        embed.add_field(name = 'dad', value = '({}dadjoke / funny)'.format(prefix), inline = True)
        embed.add_field(name = 'help', value = '({}help / cmds)'.format(prefix), inline = True)
        embed.add_field(name = 'mod', value = '({0}ban, {0}unban, {0}kick)'.format(prefix), inline = True)
        embed.add_field(name = 'ping', value = '({}ping)'.format(prefix), inline = True)
        embed.add_field(name = 'verif', value = '({}verify)'.format(prefix), inline = True)

        user = ctx.message.author

        await ctx.send(embed = embed)
    else:
        await ctx.send('Sorry, {}, you dont have permissions...'.format(ctx.message.author))

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension('cogs.{}'.format(filename[:-3]))


client.run(os.environ['token'])
