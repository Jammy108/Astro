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



    @commands.Cog.listener()
    async def on_guild_join(self, guild):

        default_prefix = utils.Config.get('default_prefix')

        #Adds guild to caches
        utils.Cache.prefixes[guild.id] = default_prefix
        utils.Cache.disabled_commands[guild.id] = []
        utils.Cache.disabled_modules[guild.id] = []

        #Adds guild to db
        await utils.db.conn.execute('INSERT INTO guilds (guild_id, prefix) VALUES ($1, $2)', guild.id, default_prefix)



    @commands.Cog.listener()
    async def on_guild_remove(self, guild):

        #Removes guild from cache
        del utils.Cache.prefixes[guild.id]
        del utils.Cache.disabled_commands[guild.id]
        del utils.Cache.disabled_modules[guild.id]

        #Removes guild from db
        await utils.db.conn.execute('DELETE FROM guilds WHERE guild_id = $1;', guild.id)





def setup(bot):
    bot.add_cog(System(bot))
