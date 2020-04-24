import asyncpg
import utils

"""
Database class for connecting,
retrieving and editing data.
"""

class Database(object):
    def __init__(self):
        super(Database, self).__init__()


    async def connect(self):
        credentials = {
            'user':utils.Config.get('dbUser'),
            'password':utils.Config.get('dbPass'),
            'database':utils.Config.get('dbName'),
            'host':utils.Config.get('dbHost')
        }


        connection = await asyncpg.create_pool(**credentials)
        self.conn = connection
