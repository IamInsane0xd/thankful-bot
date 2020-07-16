import discord
from discord.ext import commands
from discord.utils import get

class Verif(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def verify(self, ctx):
        member = ctx.message.author
        role = get(member.guild.roles, name = 'Member')
        vrole = get(member.guild.roles, name = 'Verification')
        drole1 = get(member.guild.roles, name = '-------- COLORS / SZÍNEK --------')
        drole2 = get(member.guild.roles, name = '-------- ROLES / RANGOK --------')
        drole3 = get(member.guild.roles, name = '-------- OTHER / EGYÉB --------')

        if role not in member.roles and vrole in member.roles and ctx.message.channel.id == 732691234988097557:
            try:
                await ctx.channel.purge(limit = 1)

                await member.remove_roles(vrole)
                await member.add_roles(role)
                await member.add_roles(drole1)
                await member.add_roles(drole2)
                await member.add_roles(drole3)

                await member.send('Verification succesful!\nHave a great time!')
            except:
                await member.send('Semorthing went wrong with the verification, pease try again...')

        elif role in member.roles:
            await ctx.send('You are already verified...')

            try:
                await member.remove_roles(vrole)
                await member.add_roles(drole1)
                await member.add_roles(drole2)
                await member.add_roles(drole3)
            except:
                return

        elif ctx.message.channel.id == 732691234988097557:
            await ctx.send('Wrong channel >:c')

    @commands.command()
    async def rolecheck(self, ctx):
        if ctx.message.author.guild_permissions.administrator:
            guild = ctx.message.guild
            user = ctx.message.author

            role = get(user.guild.roles, name = 'Member')
            vrole = get(user.guild.roles, name = 'Verification')
            drole1 = get(user.guild.roles, name = '-------- COLORS / SZÍNEK --------')
            drole2 = get(user.guild.roles, name = '-------- ROLES / RANGOK --------')
            drole3 = get(user.guild.roles, name = '-------- OTHER / EGYÉB --------')

            for member in guild.members:
                if vrole in member.roles:
                    return

                elif role in member.roles:
                    if drole1 not in member.roles:
                        try:
                            await member.add_roles(drole1)
                        except:
                            return

                    if drole2 not in member.roles:
                        try:
                            await member.add_roles(drole2)
                        except:
                            return

                    if drole3 not in member.roles:
                        try:
                            await member.add_roles(drole3)
                        except:
                            return

                else:
                    try:
                        await member.give_roles(vrole)
                        await member.remove_roles(drole1)
                        await member.remove_roles(drole2)
                        await member.remove_roles(drole3)
                    except:
                        return

            await ctx.send('Done!')

def setup(client):
    client.add_cog(Verif(client))
