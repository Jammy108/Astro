from discord.ext import commands


class CommandDisabled(commands.CommandError):
    def __init__(self, command):
        super().__init__(command)

class ModuleDisabled(commands.CommandError):
    def __init__(self, module):
        super().__init__(module)
