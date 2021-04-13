from discord.ext import commands
import discord
from .. import custom_decorators

# def admin_channel_check(ctx):
#         return ctx.channel.name == "admin-commands" and ctx.prefix == "+"


class server_admin(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.command(name='give_role',
    brief="Add a user to a role",
    description='''
    This command allows you to add roles to a user.
    e.g. +give_role Quiz Gordon
    ''')
    @commands.check(custom_decorators.check_admin)
    @commands.has_role('@Admin')
    async def give_role_user(self, ctx, role: discord.Role, user: discord.Member):

        await user.add_roles(role)
        await ctx.send("Role Added to {}".format(user))

    @commands.command(name='take_role',
    brief="Remove roles from User",
    description='Remove a role from a user')
    @commands.check(custom_decorators.check_admin)
    @commands.has_role('@Admin')
    async def take_role_user(self, ctx, role: discord.Role, user: discord.Member):
        await user.remove_roles(role)
        await ctx.send("Role removed from {}".format(user))

    @commands.command(name='list_roles',
    brief='Show server roles',
    description='This command will show you all roles in the server.\nUsage:')
    @commands.check(custom_decorators.check_admin)
    @commands.has_role("@Admin")
    async def list_server_roles(self, ctx):
        role_list = '\n - '.join([str(role.name) for role in ctx.guild.roles])
        await ctx.send('Server Roles:\n - {}'.format(role_list))


    @commands.command(name='list_channels',
    brief='Show server channels',
    description='This command will show all channels in the server.\nUsage:')
    @commands.check(custom_decorators.check_admin)
    @commands.has_role('@Admin')
    async def show_server_channels(self, ctx):
        chan_list = '\n - '.join([str(chan) for chan in ctx.guild.channels])
        await ctx.send('Server Channels:\n - {}'.format(chan_list))

    @commands.command(name='purge_channel',
    brief='This will clear the channel',
    description='This command will clear the entire channel of any messages')
    @commands.check(custom_decorators.check_admin)
    @commands.has_role('@Admin')
    async def clear_channel_history(self, ctx):
        limit = 0
        async for msg in ctx.channel.history(limit=None):
            limit += 1
        await ctx.channel.purge(limit=limit)

def setup(bot):
    bot.add_cog(server_admin(bot))