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
    
class Xp:
	async def defaultrole(self, ctx):
		"""Lists the default role that new users are assigned."""
		# Check if we're suppressing @here and @everyone mentions
		if self.settings.getServerStat(ctx.message.guild, "SuppressMentions").lower() == "yes":
			suppress = True
		else:
			suppress = False

		role = self.settings.getServerStat(ctx.message.guild, "DefaultRole")
		if role == None or role == "":
			msg = 'New users are not assigned a role on joining this server.'
			await ctx.channel.send(msg)
		else:
			# Role is set - let's get its name
			found = False
			for arole in ctx.message.guild.roles:
				if str(arole.id) == str(role):
					found = True
					msg = 'New users will be assigned to **{Unassigned}**.'.format(arole.name)
					# Check for suppress
					if suppress:
						msg = Nullify.clean(msg)
			if not found:
				msg = 'There is no role that matches id: `{}` - consider updating this setting.'.format(role)
			await ctx.message.channel.send(msg)
