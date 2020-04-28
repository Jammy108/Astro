import discord
from discord.ext import commands
import utils
from datetime import datetime


class utility(commands.Cog):
    """Commands to alter settings for a guild"""
    def __init__(self, bot):
        self.bot = bot


    @commands.command(usage='[@user]', aliases=['av'])
    async def avatar(self, ctx, user:discord.Member=None):
        """
        Get the avatar of a user or yourself
        """

        #If no user is specified
        if not user:
            user = ctx.author

        #Embed crafting
        avatar_url = user.avatar_url
        embed = utils.Embed(title=f"{user.name}'s Avatar", description=f"[Avatar Url]({avatar_url})")
        embed.set_footer(f'Requested by {ctx.author.name}')
        embed.timestamp=datetime.now()
        embed.set_image(url=avatar_url)
        await ctx.send(embed=embed)



    @commands.command(usage='[@user]')
    async def permissions(self, ctx, user:discord.Member=None):
        """
        List the guild permissions of a user or yourself
        """
        #If no user is specified
        if not user:
            user = ctx.author

        #Get permissions
        permissions = user.guild_permissions

        enabled = []
        disabled = []

        #Sorting of permissions
        for perm, bool in permissions:
            perm = perm.replace('_',' ').capitalize()
            if bool:
                enabled.append(perm)
            else:
                disabled.append(perm)

        #Crafting embed
        embed = utils.Embed(title=f"{user.name}'s Permissions")
        embed.set_footer(text=f'Requested by {ctx.author.name}')
        embed.timestamp=datetime.now()
        embed.add_field(name='Enabled Permissions',
            value='None' if not enabled else '\n'.join(f":green_circle: {perm}" for perm in enabled))
        embed.add_field(name='Disabled Permissions',
            value='None' if not disabled else '\n'.join(f":red_circle: {perm}" for perm in disabled))

        await ctx.send(embed=embed)





def setup(bot):
    bot.add_cog(utility(bot))
