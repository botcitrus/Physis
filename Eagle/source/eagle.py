import discord
from discord.ext import commands
import os

import config

null_color=discord.Color.from_rgb(47,49,56)

eagle = commands.Bot(command_prefix=config.PREFIX, intents=discord.Intents.all(), fetch_offline_members=True)
eagle.remove_command('help')

@eagle.command()
@commands.is_owner()
async def files(ctx):
    e = discord.Embed(title='Список файлов обнаруженных в директории `./cogs`:', color=null_color)
    for filename in os.listdir('./cogs'):
        if filename[:-3] in eagle.cogs:
            fl = discord.utils.get(eagle.emojis, name='online1')
        else:
            fl = discord.utils.get(eagle.emojis, name='dnd')
        if filename.endswith('.py'):
            e.add_field(name=filename, value=f'╰〔:page_with_curl:〕- `Размер`: {os.path.getsize(f"./cogs/{filename}") // 1024} Кбайт | `Загружен как ког:` {fl}', inline=False)
    await ctx.send(embed=e)

@eagle.command()
@commands.is_owner()
async def cog(
    ctx, 
    acti, 
    extension = None
    ):
    if extension == None:
        if acti == 'list':
            list = ", ".join([cog for cog in eagle.cogs])
            e = discord.Embed(title='Список агруженных когов:', description=f'**{list}**', color=null_color)
            await ctx.send(embed=e)
        else:   
            await ctx.message.add_reaction('⚠️')
    else:
        if acti == 'load':
            eagle.load_extension(f'cogs.{extension}')
            await ctx.message.add_reaction('✅')
        elif acti == 'reload':
            eagle.reload_extension(f'cogs.{extension}')
            await ctx.message.add_reaction('✅')
        elif acti == 'unload':
            eagle.unload_extension(f'cogs.{extension}')
            await ctx.message.add_reaction('✅')
        else:
            await ctx.message.add_reaction('⚠️')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
       eagle.load_extension(f'cogs.{filename[:-3]}')

eagle.run(config.TOKEN)
