#Imports
import discord
from discord.ext import commands
import asyncio
import utils

extensions = utils.Config.get('extensions')

#Function which starts bot
async def run():

    # Creates Astro class instance
    bot = Astro()


    # Starts bot
    try:
        token = utils.Config.get('token')
        await bot.start(token)
    except KeyboardInterrupt:
        await db.close()
        await bot.logout()




# Returns prefix from db cache
async def get_prefix(bot, message):
    if message.guild is None:
        return ''

    prefix = utils.Cache.prefixes[message.guild.id]
    return commands.when_mentioned_or(*prefix)(bot, message)



# Bot class
class Astro(commands.Bot):
    def __init__(self, **kwargs):
        super().__init__(command_prefix=get_prefix,
                         description=utils.Config.get('description'),
                         activity=discord.Game(name=utils.Config.get('activity')),
                         reconnect=True,
                         case_insensitive=True)


        # Loads cogs
        for extension in extensions:
            self.load_extension('cogs.' + extension)



    #Override bot close function
    async def close(self):

        #Close db connection
        await utils.db.conn.close()

        #Actually shutdown bot
        await super().close()





loop = asyncio.get_event_loop()
loop.run_until_complete(run())
