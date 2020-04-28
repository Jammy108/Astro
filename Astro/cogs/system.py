import discord
from discord.ext import commands
import utils


class System(commands.Cog):
    """Listeners/Commands/Functions built for the inner workings"""
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):

        #Creates database connection
        print('Connecting to database')
        await utils.db.connect()

        #Creates cache
        print('Creating cache')
        await utils.Cache.init()


        print(f'Logged in as {self.bot.user.name} | {self.bot.user.id}')




def setup(bot):
    bot.add_cog(System(bot))
