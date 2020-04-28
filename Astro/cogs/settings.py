import discord
from discord.ext import commands
import utils
import time

class settings(commands.Cog):
    """Commands to alter settings for a guild"""
    def __init__(self, bot):
        self.bot = bot


    #Changes bot prefix for the guild or says the current prefix
    @commands.has_permissions(administrator=True)
    @commands.command(usage="<prefix>")
    async def prefix(self, ctx, prefix:str = None):
        """
        Get the current prefix or change it
        """

        current_prefix = utils.Cache.prefixes[ctx.guild.id]

        #If they haven't entered a prefix
        if prefix is None:
            return await ctx.send(embed=utils.Embed(description=f'Current prefix is set to: `{current_prefix}`'))


        #if prefix is bigger than max prefix length setting
        if len(prefix) > utils.Config.get('max_prefix_length'):
            return await ctx.send(embed=utils.Embed(description=f'The max prefix length is {max_prefix_length}'))


        #If trying to change to current prefix
        if prefix == current_prefix:
            return await ctx.send(embed=utils.Embed(description=f'The prefix is already set to `{current_prefix}`'))


        #Update cache + database with new prefix
        utils.Cache.prefixes[ctx.guild.id] = prefix
        await utils.db.conn.execute('UPDATE guilds SET prefix = $1 WHERE guild_id = $2', prefix, ctx.guild.id)


        await ctx.send(embed=utils.Embed(description=f'Prefix changed to `{prefix}`'))



def setup(bot):
    bot.add_cog(settings(bot))
