######################################
import discord
from discord.ext import commands
from os import listdir as ld
import os
import asyncio
import random
######################################-<'импортры'

######################################
null_color=discord.Color.from_rgb(47,49,56)
######################################

client = commands.Bot(command_prefix='.')#-<установка префикса

@client.event#-<создание 
async def on_ready():
    await client.change_presence(activity=discord.Streaming(name="Physis", url="https://www.twitch.tv/qrushcsgo"))#-<сделал активность ,чтоб бот стримил
    print('——————————————————————\nPhysis Beta [ON]\n——————————————————————')

# я предлагаю тебе сделать коги и щас я покажу как это всё легко делается!
# преждем чем начать создавать файлы с командами тебе нужно написать несколько команд!

@client.command()
@commands.is_owner()
async def files(ctx):
    embed = discord.Embed(title='Список файлов обнаруженных в директории `./cogs`:', color=null_color)
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            if f"cogs.{filename[:-3]}" in client.extensions:
                switcher = discord.utils.get(client.emojis, name="da")
            else:
                switcher = discord.utils.get(client.emojis, name="net")
            embed.add_field(name=filename, value=f'╰〔:page_with_curl:〕- `Размер`: {os.path.getsize(f"./cogs/{filename}") // 1024} Кбайт | `Загружен как ког:` {switcher}', inline=False)
    await ctx.reply(embed=embed, mention_author=False)

@client.command()
@commands.is_owner()
async def cog(
    ctx, 
    acti, 
    extension = None
    ):
    if extension == None:
        if acti == 'list':
            list = ", ".join([cog for cog in client.cogs])
            e = discord.Embed(title='Список агруженных когов:', description=f'**{list}**', color=null_color)
            await ctx.send(embed=e)
        else:   
            await ctx.message.add_reaction('⚠️')
    else:
        if acti == 'load':#загрузить ког
            client.load_extension(f'cogs.{extension}')
            await ctx.message.add_reaction('✅')
        elif acti == 'reload':#перезагрузить ког
            client.reload_extension(f'cogs.{extension}')
            await ctx.message.add_reaction('✅')
        elif acti == 'unload':#отгрузить ког
            client.unload_extension(f'cogs.{extension}')
            await ctx.message.add_reaction('✅')
        else:
            await ctx.message.add_reaction('⚠️')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
       client.load_extension(f'cogs.{filename[:-3]}')#вот это запустит твои коги

client.run("ODgyNjE4NDI1Mjc5NjcyMzYw.YS-Adg.LaWuUDXpK5_Z-SdJ2twmP-HYTnU")