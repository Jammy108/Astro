import discord
from discord.ext import commands
from datetime import datetime
import traceback
import utils


class Errors(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #Method to built embed
    def build_embed(self, title, description):
        embed = utils.Embed(title=title, description=description, timestamp=datetime.now())
        return embed


    #Called when there is a command error
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):

        #Gets the error
        error = getattr(error, 'original', error)

        #Error text
        error_txt = str(error).capitalize()

        #Errors to ignore
        ignored = (commands.CommandNotFound)

        #Errors relating to bad format
        format_errors = (commands.MissingRequiredArgument, commands.BadArgument,
                         commands.BadUnionArgument, commands.TooManyArguments)


        if isinstance(error, ignored):
            return



        #If the error is to do with bad format
        elif isinstance(error, format_errors):
            embed = self.build_embed('Format Error', f'Please use the correct format:\n ```{ctx.command} {ctx.command.usage}```')
            return await ctx.send(embed=embed)


        #If the user has low/missing permissions
        elif isinstance(error, commands.MissingPermissions):
            missing_perms = '\n'.join(error.missing_perms)
            embed = self.build_embed('Permission Error', f'You do not have the permissions required to run this command:\n ```{missing_perms}```')
            return await ctx.send(embed=embed)



        #If the bot has low permissions
        elif isinstance(error, commands.BotMissingPermissions):
            missing_perms = '\n'.join(error.missing_perms)
            embed = self.build_embed('Bot Permission Errorr', f'I do not have the permissions required to run this command:\n ```{missing_perms}```')
            return await ctx.send(embed=embed)


        #If the user is missing a required role
        elif isinstance(error, commands.MissingRole):
            embed = self.build_embed('Missing Role Error', f'You do not have the role required to run this command:\n ```{error.missing_role}```')
            return await ctx.send(embed=embed)


        #If the bot is missing a required role
        elif isinstance(error, commands.BotMissingRole):
            embed = self.build_embed('Missing Role Error', f'I do not have the role required to run this command:\n ```{error.missing_role}```')
            return await ctx.send(embed=embed)



        #If the user is missing all of the roles required
        elif isinstance(error, commands.MissingAnyRole):
            missing_roles = '\n'.join(str(role) for role in list(error.missing_roles))
            embed = self.build_embed('Missing Roles Error', f'You do not have any of the required roles to run this command: ```\n{missing_roles}\n```')
            return await ctx.send(embed=embed)



        #If the bot is missing all of the roles required
        elif isinstance(error, commands.BotMissingAnyRole):
            missing_roles = '\n'.join(str(role) for role in list(error.missing_roles))
            embed = self.build_embed('Missing Roles Error', f'I do not have any of the required roles to run this command: ```\n{missing_roles}\n```')
            return await ctx.send(embed=embed)


        #If the command is disabled
        elif isinstance(error, commands.DisabledCommand):
            embed = self.build_embed('Disabled Command Error', 'This command is currently disabled, we hope to enable it again soon')
            return await ctx.send(embed=embed)


        #If the command cannot be used in private message
        elif isinstance(error, commands.NoPrivateMessage):
            try:
                embed = self.build_embed('Private Message Error', 'This command cannot be used through private message')
                return await ctx.author.send(embed=embed)
            except:
                pass


        #If the command requires the owner to run it
        elif isinstance(error, commands.NotOwner):
            embed = self.build_embed('Not Owner Error', 'This command is only for the bot owner/developers')
            return await ctx.send(embed=embed)


        #If the command required an NSFW channel
        elif isinstance(error, commands.NSFWChannelRequired):
            embed = self.build_embed('NSFW Channel Error', 'This command can only be used in channels marked as NSFW')
            return await ctx.send(embed=embed)



        #If the error isn't any of the above
        traceback_text = ''.join(traceback.format_exception(type(error),  error, error.__traceback__, 1))
        embed = self.build_embed('Uncaught Error', f'Full traceback:```python\n{traceback_text}\n```')
        embed.set_footer(text='Developers have been notified')
        await ctx.send(embed=embed)





def setup(bot):
    bot.add_cog(Errors(bot))
