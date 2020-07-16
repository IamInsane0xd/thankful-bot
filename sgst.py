import discord
from discord.ext import commands
from discord.utils import get

class Sgst(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def suggest(self, ctx, type = None, *, sgst = None):
        if type == "server" or type == "bot":
            if type == 'server':
                channel = get(ctx.message.guild.channels, name = 'server-suggestions')

                await channel.send('New **server-suggestion** from *{}*:\n```{}```'.format(str(ctx.message.author)[:-5], sgst))

            if type == 'bot':
                channel = get(ctx.message.guild.channels, name = 'bot-suggestions')

                await channel.send('New **server-suggestion** from *{}*:\n```{}```'.format(str(ctx.message.author)[:-5], sgst))

        else:
            await ctx.send('Please use the correct format: `t.suggest <server|bot> <suggestion>`')

def setup(client):
    client.add_cog(Sgst(client))
