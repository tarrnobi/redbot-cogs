import discord
from discord.ext import commands

class YT:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="yt")
    async def yt(self):
        """This does stuff!"""

        #Your code will go here
        await self.bot.say("I can do stuff!")

def setup(bot):
    bot.add_cog(Mycog(bot))
