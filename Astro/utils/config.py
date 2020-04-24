from pathlib import Path
import yaml


"""
Config Class for retrieving,
sorting and editing the bot's
config.yml file.
"""

class Config(object):
    def __init__(self):
        super(Config, self).__init__()

        #Path to config file
        self.path = str(Path(__file__).parents[1]) + '\\config.yml'

        #Sorted config data
        self.data = {}

        self.open()


    #Opens yml file
    def open(self):
        #Returns a dict of values
        with open(self.path) as f:
            config = yaml.load(f, Loader=yaml.FullLoader)
        self.sort(config)


    #Retrieves nested dictionary values + keys
    def sort(self, dict):
        for k, v in dict.items():
            if isinstance(v, type({})):
                self.sort(v)
            else:
                self.data[k] = v


    #Gets value from config (returns None if nothing found)
    def get(self, value):
        return self.data.get(value, None)
