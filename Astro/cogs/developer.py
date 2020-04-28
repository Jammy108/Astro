import discord
from discord.ext import commands
import utils


class Developer(commands.Cog):
    """Commands built for Astro developers/owners"""
    def __init__(self, bot):
        self.bot = bot


    #Checks if author is bot owner for all cog commands
    async def cog_check(self, ctx):
        if not await self.bot.is_owner(ctx.author):
            raise commands.NotOwner
        return True



    #Shutsdown bot
    @commands.command()
    async def shutdown(self, ctx):
        """
        Shuts down the bot
        """
        await ctx.send(embed=utils.Embed(description='Shutting down'))
        await self.bot.close()


    #Reloads a cog
    @commands.command(usage="[cog]")
    async def reload(self, ctx, cog: str):
        """
        Reload a cog
        """
        try:
            self.bot.reload_extension("cogs." + cog)
        except Exception as e:
            embed = utils.Embed(description=f"Error: {e}")
        else:
            embed = utils.Embed(description=f"The {cog.capitalize()} cog has been reloaded")
        finally:
            await ctx.send(embed=embed)



    #Loads a cog
    @commands.command(usage="[cog]")
    async def load(self, ctx, cog: str):
        """
        Load a cog
        """
        try:
            self.bot.load_extension("cogs." + cog)
        except Exception as e:
            embed = utils.Embed(description=f"Error: {e}")
        else:
            embed = utils.Embed(description=f"The {cog.capitalize()} cog has been loaded")
        finally:
            await ctx.send(embed=embed)



    #Unloads a cog
    @commands.command(usage="[cog]")
    async def unload(self, ctx, cog: str):
        """
        Unload a cog
        """
        try:
            self.bot.unload_extension("cogs." + cog)
        except Exception as e:
            embed = utils.Embed(description=f"Error: {e}")
        else:
            embed = utils.Embed(description=f"The {cog.capitalize()} cog has been unloaded")
        finally:
            await ctx.send(embed=embed)





def setup(bot):
    bot.add_cog(Developer(bot))
