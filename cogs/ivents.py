import discord
from discord.ext import commands
import random

base_color=0xACE1AF

class Iven(commands.Cog):
    def __init__(self, client):
        self.client = client
	
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        for channel in guild.text_channels:
            if channel.permissions_for(guild.me).send_messages:
                embed = discord.Embed(title = ' Thanks for adding Physis', description = '`-` Use `.хелп` to view all of my commands\n`-` You can change my prefix from `.` by using `.prefix`\n`-` If you need more help, please visit my support server||no link||\nto add a bot, follow the ||no link||\n▬▬▬▬▬▬▬▬▬▬▬▬▬\n**Physis Premium in development**', color=0xEE82EE)
                await channel.send(embed=embed)
            break

    @commands.command()
    async def flip(self,ctx):
        coin = random.choice(['орёл', 'решка'])
        embed = discord.Embed(title='Орёл решка',description=f'Сверху на монетке выпало: {coin}',color=base_color)
        await ctx.send(embed=embed)


def setup(client):
	client.add_cog(Iven(client))