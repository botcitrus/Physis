import discord
from discord.ext import commands
from discord.ext.commands.core import bot_has_guild_permissions
from datetime import datetime
import typing as t

base_color=0xACE1AF
su_color=0xACE1AF
err_color=0xACE1AF

class Iven(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    @commands.has_guild_permissions(kick_members=True)
    async def kick(self, ctx, members: commands.Greedy[discord.Member] = None, *, res: t.Optional[str] = 'Не указана.'):
        if member == None:
            e = discord.Embed(
                title=f'Вы не указали параметр:',
                description='> Пользователь/ли',
                color=err_color
            )
            await ctx.send(embed=e)
        else:
            await member.kick(reason = res)
            e = discord.Embed(
                title=f'Пользователь выгнан с сервера.',
                description=f'''`Пользователь`: {member.mention}
`Причина`: {res}
`Модератор`: {ctx.author.mention}''',
                color=su_color,
                timestamp=datetime.utcnow()
            )
            await ctx.send(embed=e)

    @commands.command()
    @commands.has_guild_permissions(ban_members=True)
    async def ban(self, ctx, members: commands.Greedy[discord.Member] = None, *, res: str = 'Не указана.'):
        if member == None:
            e = discord.Embed(
                title=f'Вы не указали параметр:',
                description='> Пользователь/ли',
                color=err_color
            )
            await ctx.send(embed=e)
        else:
            await member.ban(reason = res)
            e = discord.Embed(
                title=f'Пользователь забанен.',
                description=f'''`Пользователь`: {member.mention}
`Причина`: {res}
`Модератор`: {ctx.author.mention}''',
                color=su_color,
                timestamp=datetime.utcnow()
            )
            await ctx.send(embed=e)

    @commands.command()
    @commands.has_guild_permissions(manage_messages=True)
    async def clean(self, ctx, amount: int = 0):
        if amount > 3500:
            e = discord.Embed(
                title=f'Невозможно совершить операцию',
                description=f'Указан слишком большой параметр сообщений. Вы можете указать число сообщений не меньше 0 и не больше 3500.',
                color=err_color
            )
            await ctx.send(embed=e)
        else:
            await ctx.channel.purge(limit=amount+1)
            e = discord.Embed(
                title=f'Успешно!',
                description=f'''`Пользователем`: {ctx.author.mention}
`Удалено сообщений`: {amount}''',
                color=su_color,
                timestamp=datetime.utcnow()
            )
            await ctx.send(embed=e)


def setup(client):
	client.add_cog(Iven(client))