import discord
from discord.ext import commands
import json

base_color=0x3498db
err_color=0xe74c3c

class ivents(commands.Cog):
    def __init__(self, Bot):
        self.Bot = Bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'''
 ________                     ______      _            ________
|  ______|       /\          /  ___ \    | |          |  ______|
| |             /  \        /  /   \_\	 | |          | |
| |____        /  _ \       |  |	 | |          | |____
|  ____|      /  /_\ \      |  |   __	 | |          |  ____|
| |          /  ____  \     |  |  |_ |   | |          | |
| |______   /  /    \  \    \  \___/ /	 | |_______   | |______
|________| /__/      \__\    \______/    |_________|  |________|

Зарегистрирован как:   [[{self.Bot.user}]]''')
        await self.Bot.change_presence(
            status=discord.Status.idle,
            activity=discord.Activity(
                type=discord.ActivityType.watching, 
                name='sts'
            )
        )

def setup (Bot):
    Bot.add_cog(ivents(Bot))
