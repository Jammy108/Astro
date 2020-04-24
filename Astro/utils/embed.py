import discord
import utils
from datetime import datetime

"""
Custom embed class to set
default colour and timestamp
"""

class Embed(discord.Embed):
    def __init__(self, **attrs):
        attrs.setdefault('colour', utils.Config.get('embed_colour'))
        attrs.setdefault('timestamp', datetime.now())
        super().__init__(**attrs)
