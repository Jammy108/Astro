import discord
from discord.ext import commands
from datetime import datetime
import utils


class Developer(commands.Cog):
    """Commands built for Astro developers/owners"""
    def __init__(self, bot):
        self.bot = bot


    #Shutsdown bot
    @commands.is_owner()
    @commands.command(description="Shutdown the bot")
    async def shutdown(self, ctx):
        embed = utils.Embed(description='Shutting down')
        await ctx.send(embed=embed)
        await self.bot.close()


    #Reloads a cog
    @commands.is_owner()
    @commands.command(description="Reload a cog", usage="[cog]")
    async def reload(self, ctx, cog: str):
        try:
            self.bot.unload_extension("cogs." + cog)
            self.bot.load_extension("cogs." + cog)
        except Exception as e:
            embed = utils.Embed(description=f"Error: {e}")
        else:
            embed = utils.Embed(description=f"The {cog.capitalize()} cog has been reloaded")
        finally:
            await ctx.send(embed=embed)



    #Reloads a cog
    @commands.is_owner()
    @commands.command(description="Load a cog", usage="[cog]")
    async def load(self, ctx, cog: str):
        try:
            self.bot.load_extension("cogs." + cog)
        except Exception as e:
            embed = utils.Embed(description=f"Error: {e}")
        else:
            embed = utils.Embed(description=f"The {cog.capitalize()} cog has been loaded")
        finally:
            await ctx.send(embed=embed)



    #Reloads a cog
    @commands.is_owner()
    @commands.command(description="Load a cog", usage="[cog]")
    async def unload(self, ctx, cog: str):
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
