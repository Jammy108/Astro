#Imports
import discord
from discord.ext import commands
import asyncio
import utils


extensions = utils.Config.get('extensions')

#Function which starts bot
async def run():

    #Creates database connection
    await utils.db.connect()

    #Creates database cache
    await utils.Cache.create()

    # Creates Astro class instance
    bot = Astro()

    # Starts bot
    try:
        await bot.start(utils.Config.get('token'))
    except KeyboardInterrupt:
        await db.close()
        await bot.logout()


# Returns prefix from db cache
async def get_prefix(bot, message):
    prefix = utils.Cache.get_prefix(message.guild.id)
    return commands.when_mentioned_or(prefix)(bot, message)


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

    #Called when the bot is ready
    async def on_ready(self):
        print(f'Logged in as {self.user.name} | {self.user.id}')


loop = asyncio.get_event_loop()
loop.run_until_complete(run())
