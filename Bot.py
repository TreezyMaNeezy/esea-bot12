from discord import *
from discord.ext import commands

class Control:
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(pass_context=True)
    async def lock(self, context) :
        """Locks a channel."""
        channel = context.message.author.voice_channel

        await bot.edit_channel(channel, user_limit=len(channel.voice_members))
        await bot.send_message(context.message.channel, "{} has been locked.".format(channel.name))

    @commands.command(pass_context=True)
    async def unlock(self, context):
        """Locks a channel."""
        channel = context.message.author.voice_channel

        await bot.edit_channel(channel, user_limit=0)
        await bot.send_message(context.message.channel, "{} has been unlocked.".format(channel.name))


bot = commands.Bot(command_prefix=commands.when_mentioned_or("-"))
bot.add_cog(Control(bot))

@bot.event
async def on_ready():
    print("Logged in as")
    print(bot.user.name)
    print(bot.user.id)
    print("------")

if __name__ == "__main__" :
    bot.run("Mzc3ODc4ODMzOTI5NjUwMTc2.DOTWmg.1Sip3uihH1F-OG5DfXpraAx7PxI") # Put bot token here
