import discord
from discord.ext import commands

class Ping(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        await ctx.send('Pong! (ping is: {0}ms)'.format(round(self.client.latency * 1000)))

def setup(client):
    client.add_cog(Ping(client))
