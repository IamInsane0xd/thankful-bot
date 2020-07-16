import discord
from discord.ext import commands
from discord.utils import get

class Sgst(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def suggest(self, ctx, type = None, *, sgst = None):
        try:
            await ctx.channel.purge(limit = 1)
        except discord.Forbidden:
            print("Cant delete message >:c")
            print('')

        if ctx.message.channel.id == 732713710115618866:
            if type == "server" or type == "bot":
                if sgst == None
                    await ctx.send('Please use the correct format: `t.suggest <server|bot> <suggestion>`')

                else:
                    if type == 'server':
                        channel = get(ctx.message.guild.channels, name = 'server-suggestions')

                        await channel.send('New **server-suggestion** from *{}*:\n```{}```'.format(str(ctx.message.author)[:-5], sgst))

                    if type == 'bot':
                        channel = get(ctx.message.guild.channels, name = 'bot-suggestions')

                        await channel.send('New **server-suggestion** from *{}*:\n```{}```'.format(str(ctx.message.author)[:-5], sgst))
            else:
                await ctx.send('Please use the correct format: `t.suggest <server|bot> <suggestion>`')
        else:
            await ctx.send("Don't use commands in wrong channel >:c")

def setup(client):
    client.add_cog(Sgst(client))
