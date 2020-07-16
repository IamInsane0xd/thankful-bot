import discord
from discord.ext import commands
from discord.utils import get

class Clr(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def nuke(self, ctx):
        if ctx.message.author.guild_permissions.manage_messages:
            ammount = 9999999

            await ctx.send('__Launching nukes!__')
            await ctx.channel.purge(limit = ammount)
            await ctx.send('*{}* has turned this channel into **hirosima v2**\nhttps://imgur.com/LIyGeCR'.format(ctx.message.author.mention))
            channel = get(ctx.message.author.guild.channels, name = "logz")
            await channel.send ('*{}* nuked channel *{}*'.format(ctx.message.author.mention, ctx.message.channel))
        else:
            await ctx.send('Sorry, {}, you dont have permissions...'.format(ctx.message.author.mention))

    @commands.command(aliases = ['purge'])
    async def clear(self, ctx, ammount = 0):
        if ctx.message.author.guild_permissions.manage_messages:
            await ctx.channel.purge(limit = ammount + 1)
            channel = get(ctx.message.author.guild.channels, name = "logz")
            await channel.send ('*{}* cleared *{} message(s)* from *{}*'.format(ctx.message.author.mention, ammount, ctx.message.channel))
        else:
            await ctx.send('Sorry, {}, you dont have permissions...'.format(ctx.message.author.mention))
def setup(client):
    client.add_cog(Clr(client))
