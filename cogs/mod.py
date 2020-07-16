import discord
from discord.ext import commands
from discord.utils import get

class Mod(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def kick(self, ctx, member : discord.Member = None, *, reason = None):
        if ctx.message.author.guild_permissions.kick_members:
            if member != None:
                try:
                    await member.kick(reason = reason)
                    await ctx.channel.purge(limit = 1)
                    await ctx.send('Succesfuly **kicked** *{}* for reason: *{}*.'.format(member, reason))
                    channel = get(ctx.message.author.guild.channels, name = "logz")
                    await channel.send ('*{}* kicked *{}* for *{}*'.format(ctx.message.author.mention, member.mention, reason))
                except discord.Forbidden:
                    await ctx.send("Sorry, but I can't kick *{}*, or I dont have `kick_members` permission...".format(str(member)[:-5]))
            else:
                await ctx.send('Please mention a user to kick.')
        else:
            await ctx.send('Sorry, {}, you dont have permissions...'.format(ctx.message.author.mention))

    @commands.command()
    async def ban(self, ctx, member : discord.Member = None, *, reason = None):
        if ctx.message.author.guild_permissions.ban_members:
            if member != None:
                try:
                    await member.ban(reason = reason)
                    await ctx.channel.purge(limit = 1)
                    await ctx.send('Succesfuly **banned** *{}* for reason: *{}*.'.format(member, reason))
                    channel = get(ctx.message.author.guild.channels, name = "logz")
                    await channel.send ('*{}* banned *{}* for *{}*'.format(ctx.message.author.mention, member.mention, reason))
                except discord.Forbidden:
                    await ctx.send("Sorry, but I can't kick *{}*, or I dont have `ban_members` permission...".format(str(member)[:-5]))
            else:
                await ctx.send('Please mention a user to ban.')
        else:
            await ctx.send('Sorry, {}, you dont have permissions...'.format(ctx.message.author.mention))

    @commands.command()
    async def unban(self, ctx, *, member = None):
        if ctx.message.author.guild_permissions.ban_members:
            if member != None:
                banned = await ctx.guild.bans()
                member_name, member_disc = member.split('#')

                for ban_entry in banned:
                    user = ban_entry.user

                    if (user.name, user.discriminator) == (member_name, member_disc):
                        try:
                            await ctx.guild.unban(user)
                            await ctx.channel.purge(limit = 1)
                            await ctx.send('Succesfuly **unbanned** *{}*'.format(user.mention))
                            channel = get(ctx.message.author.guild.channels, name = "logz")
                            await channel.send ('*{}* unbanned *{}*'.format(ctx.message.author.mention, member))
                            return
                        except discord.Forbidden:
                            await ctx.send("Sorry, but I can't kick *{}*, or I dont have `ban_members` permission...".format(str(member)[:-5]))
            else:
                await ctx.send('Please specify a user to unban.')
        else:
            await ctx.send('Sorry, {}, you dont have permissions...'.format(ctx.message.author.mention))

def setup(client):
    client.add_cog(Mod(client))
