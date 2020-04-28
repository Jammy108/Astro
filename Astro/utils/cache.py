import utils

"""
Cache class that contains certain functions related
to the cache, such as changing it, fetching
prefix etc.
"""

class Cache:
    def __init__(self):
        super(Cache, self).__init__()
        self.prefixes = {}
        self.disabled_commands = {}
        self.disabled_modules = {}


    #Creates cache
    async def init(self):

        #Fetch all prefixes from database and add them to cache
        data = await utils.db.conn.fetch(f'SELECT guild_id, prefix, disabled_commands, disabled_cogs FROM guilds')

        for guild in data:
            guild_id = guild['guild_id']

            #Add prefix to prefix cache
            self.prefixes[guild['guild_id']] = guild['prefix']


            #Add disabled commands to disabled commands cache
            self.disabled_commands[guild_id] = guild['disabled_commands']


            #Add disabled cogs to disabled cogs cache
            self.disabled_modules[guild_id] = guild['disabled_cogs']
