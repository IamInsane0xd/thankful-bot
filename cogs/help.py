import discord
from discord.ext import commands

class Help(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ['cmds'])
    async def help(self, ctx):
        prefix = "t."

        embed = discord.Embed(title = 'Help', description = 'All the commands you can use:', colour = discord.Color.red())

        embed.add_field(name = '{}8ball <question>'.format(prefix), value = "it's an 8ball, what do you think it'll do", inline = False)
        embed.add_field(name = '{}dadjoke / funny'.format(prefix), value = "tells you a dad joke", inline = False)
        embed.add_field(name = '{}ping'.format(prefix), value = "check the bot's ping", inline = False)
#        embed.add_field(name = '{}meme'.format(prefix), value = "gives you a random meme from reddit (not done)", inline = False)

        if ctx.message.author.guild_permissions.manage_messages:
            embed.add_field(name = '{}clear / purge <ammount>'.format(prefix), value = "deletes a given ammount of messages", inline = False)
            embed.add_field(name = '{}nuke'.format(prefix), value = "nukes a channel to the best of it's abilities", inline = False)

        if ctx.message.author.guild_permissions.kick_members:
            embed.add_field(name = '{}kick <user> <reason*>'.format(prefix), value = "what do u fucking think it'll do", inline = False)

        if ctx.message.author.guild_permissions.ban_members:
            embed.add_field(name = '{}ban <user> <reason*>'.format(prefix), value = "kick but better", inline = False)
            embed.add_field(name = '{}uban <user (username#id)>'.format(prefix), value = "opposite of ban", inline = False)

        if ctx.message.author.guild_permissions.administrator:
            embed.add_field(name = '{}embed'.format(prefix), value = "lists more stuff", inline = False)

        await ctx.send(embed = embed)

def setup(client):
    client.add_cog(Help(client))
