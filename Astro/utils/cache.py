import utils

"""
Cache class that contains certain functions related
to the cache, such as changing it, fetching
prefix etc.
"""

class Cache(object):

    def __init__(self):
        super(Cache, self).__init__()
        self.guilds = {}
        self.members = {}


    #Creates initial cache from database (Should be called once)
    async def create(self):

        data = await utils.db.conn.fetch(f"SELECT guild_id, prefix, disabled_commands, disabled_cogs FROM guilds;")
        for guild in data:
            self.guilds[guild['guild_id']] = {
                key: guild[key] for key in guild.keys()
                }



    #Dumps cache into database
    def dump(self):
        pass


    #Updates guild info within cache
    def update_guild(self, guild_id, data):
        for key in data:
            if key in self.guilds[guild_id]:
                self.guilds[guild_id][key] = data[key]
            else:
                pass


    #Fetches prefix for a guild
    def get_prefix(self, guild_id):
        return self.guilds[guild_id]['prefix']



    #Adds member into member cache
    def add_member(self, member):
        default_balance = utils.Config.get('default_balance', 1000)
        self.members[member.id] = {'member_id': member.id, 'guild_id': member.guild.id, 'balance': default_balance, 'offences': None, 'notes': None}



    #Adds guild into guild cache
    def add_guild(self, guild_id):
        default_prefix = utils.Config.get('default_prefix', 'a?')
        self.guilds[guild_id] = {'guild_id': guild_id, 'prefix': default_prefix, 'disabled_commands': None, 'disabled_cogs': None}
