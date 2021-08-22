import discord
from discord.ext import commands
import time
import tracemalloc
import json

tracemalloc.start()

su_color=0x2ecc71
err_color=0xe74c3c
null_color=discord.Color.from_rgb(47,49,56)

class root(commands.Cog):
    def __init__(self, Bot):
        self.Bot = Bot

    ###TECH###
    @commands.command()
    async def status(
        self,
        ctx,
        sts: str = None
    ):
        with open('databases/server_settings/mass_db.json', 'r') as f:
            server = json.load(f)
        with open('databases/users_settings/user_db.json', 'r') as f:
            usr = json.load(f)
        err = discord.utils.get(self.Bot.emojis, name='cfalse')
        tru = discord.utils.get(self.Bot.emojis, name='ctrue')
        if str(ctx.author.id) in usr["root"]:
            if sts == None:
                e = discord.Embed(
                    title=f'{err} Вы не указали параметр:',
                    description=f'Текст',
                    color=err_color
                )
                if str(ctx.guild.id) in server["reply"]:
                    await ctx.send(embed=e)
                else:
                    await ctx.reply(embed=e, mention_author=False)
            else:
                await self.Bot.change_presence(
                    status=discord.Status.idle,
                    activity=discord.Activity(
                        type=discord.ActivityType.watching, 
                        name=sts
                    )
                )
                e = discord.Embed(
                    title=f'{tru} Успешно!',
                    description=f'Статус успешно изменен на __{sts}__',
                    color=null_color
                )
                if str(ctx.guild.id) in server["reply"]:
                    await ctx.send(embed=e)
                else:
                    await ctx.reply(embed=e, mention_author=False)
        else:
            e = discord.Embed(
                title=f'{err} Отказано в доступе!',
                description=f'Получите **root** для управления этой командой.',
                color=err_color
            )
            if str(ctx.guild.id) in server["reply"]:
                await ctx.send(embed=e)
            else:
                await ctx.reply(embed=e, mention_author=False)

    @commands.command()
    @commands.is_owner()
    async def update(
        self,
        ctx,
        num,
        numname,
        date,
        *,
        txt
    ):
        wt = discord.utils.get(self.Bot.emojis, name='cnone')
        e = discord.Embed(
            title=f'{wt} UPDATE №{num} - {numname} от {date}',
            description=txt,
            color=null_color
        )
        await ctx.message.delete()
        await ctx.send('<@&846307638210723880>', embed=e)

    @commands.command()
    @commands.is_owner()
    async def rootuser(
        self,
        ctx,
        type = None,
        member: discord.Member = None
    ): 
        with open('databases/server_settings/mass_db.json', 'r') as f:
            server = json.load(f)
        with open('databases/users_settings/user_db.json', 'r') as f:
            usr = json.load(f)
        err = discord.utils.get(self.Bot.emojis, name='cfalse')
        tru = discord.utils.get(self.Bot.emojis, name='ctrue')
        if type == None and member == None:
            e = discord.Embed(
                title=f'{err} Вы не указали параметр:',
                description='''> Действие (-add/-rem) 
> Пользователь''',
                color=err_color
            )
            if str(ctx.guild.id) in server["reply"]:
                await ctx.send(embed=e)
            else:
                await ctx.reply(embed=e, mention_author=False)
        elif not type == None and member == None:
            e = discord.Embed(
                title=f'{err} Вы не указали параметр:',
                description='> Пользователь',
                color=err_color
            )
            if str(ctx.guild.id) in server["reply"]:
                await ctx.send(embed=e)
            else:
                await ctx.reply(embed=e, mention_author=False)
        else:
            if type == '-add':
                if not str(member.id) in usr["root"]:
                    usr["root"][str(member.id)] = True
                    with open('databases/users_settings/user_db.json', 'w') as f:
                        json.dump(usr, f)
                    e = discord.Embed(
                        title=f'{tru} Успешно!',
                        description=f'Пользователь {member.mention} добавлен в список **root-пользователей**.',
                        color=null_color
                    )
                    e.set_footer(text='Будьте осторожены при назначении root-пользователей! Root-пользователь имеет практически полный доступ к закрытым функциям бота.')
                    if str(ctx.guild.id) in server["reply"]:
                        await ctx.send(embed=e)
                    else:
                        await ctx.reply(embed=e, mention_author=False)
                else:
                    e = discord.Embed(
                        title=f'{err} Ошибка!',
                        description=f'Пользователь {member.mention} уже есть в списке **root-пользователей**.',
                        color=err_color
                    )
                    e.set_footer(text='Будьте осторожены при назначении root-пользователей! Root-пользователь имеет практически полный доступ к закрытым функциям бота.')
                    if str(ctx.guild.id) in server["reply"]:
                        await ctx.send(embed=e)
                    else:
                        await ctx.reply(embed=e, mention_author=False)
            elif type == '-rem':
                if str(member.id) in usr["root"]:
                    del usr["root"][str(member.id)]
                    with open('databases/users_settings/user_db.json', 'w') as f:
                        json.dump(usr, f)
                    e = discord.Embed(
                        title=f'{tru} Успешно!',
                        description=f'Пользователь {member.mention} удален из списка **root-пользователей**.',
                        color=null_color
                    )
                    e.set_footer(text='Будьте осторожены при назначении root-пользователей! Root-пользователь имеет практически полный доступ к закрытым функциям бота.')
                    if str(ctx.guild.id) in server["reply"]:
                        await ctx.send(embed=e)
                    else:
                        await ctx.reply(embed=e, mention_author=False)
                else:
                    e = discord.Embed(
                        title=f'{tru} Ошибка!',
                        description=f'Пользователя {member.mention} нету списке **root-пользователей**.',
                        color=err_color
                    )
                    e.set_footer(text='Будьте осторожены при назначении root-пользователей! Root-пользователь имеет практически полный доступ к закрытым функциям бота.')
                    if str(ctx.guild.id) in server["reply"]:
                        await ctx.send(embed=e)
                    else:
                        await ctx.reply(embed=e, mention_author=False)

    ###ITEMS###
    @commands.command()
    @commands.is_owner()
    async def item(
        self,
        ctx,
        act = None,
        it = None,
        member: discord.Member = None
    ):     
        with open('databases/server_settings/mass_db.json', 'r') as f:
            server = json.load(f)
        err = discord.utils.get(self.Bot.emojis, name='cfalse')
        tru = discord.utils.get(self.Bot.emojis, name='ctrue')
        if act == None and it == None and member == None:
            e = discord.Embed(
                    title=f'{err} Вы не указали параметр:',
                    description='''> Действие (-add/-rem)
> Предмет 
> Пользователь''',
                    color=err_color
                )
            if str(ctx.guild.id) in server["reply"]:
                await ctx.send(embed=e)
            else:
                await ctx.reply(embed=e, mention_author=False)
        if not act == None and it == None and member == None:
            e = discord.Embed(
                    title=f'{err} Вы не указали параметр:',
                    description='''> Предмет 
> Пользователь''',
                    color=err_color
                )
            if str(ctx.guild.id) in server["reply"]:
                await ctx.send(embed=e)
            else:
                await ctx.reply(embed=e, mention_author=False)
        if not act == None and not it == None and member == None:
            e = discord.Embed(
                title=f'{err} Вы не указали параметр:',
                description='> Пользователь',
                color=err_color
            )
            if str(ctx.guild.id) in server["reply"]:
                await ctx.send(embed=e)
            else:
                await ctx.reply(embed=e, mention_author=False)
        with open('databases/users_settings/user_db.json', 'r') as f:
            usr = json.load(f)
        if act == '-add':
            if str(it) in usr["items"]:
                if str(member.id) in usr["items"][str(it)]:
                    e = discord.Embed(
                        title=f'{err} Ошибка!',
                        description=f'Предмет "{it}" уже есть у {member.mention}!',
                        color=err_color
                    )
                    if str(ctx.guild.id) in server["reply"]:
                        await ctx.send(embed=e)
                    else:
                        await ctx.reply(embed=e, mention_author=False)
                else:
                    usr["items"][str(it)][str(member.id)] = True
                    with open('databases/users_settings/user_db.json', 'w') as f:
                        json.dump(usr, f) 
                    e = discord.Embed(
                        title=f'{tru} Успешно!',
                        description=f'Предмет "{it}" добавлен {member.mention}!',
                        color=su_color
                    )
                    if str(ctx.guild.id) in server["reply"]:
                        await ctx.send(embed=e)
                    else:
                        await ctx.reply(embed=e, mention_author=False)
            else:
                e = discord.Embed(
                    title=f'{err} Ошибка!',
                    description=f'Предмета "{it}" нет в списке всех предметов!',
                    color=err_color
                )
                if str(ctx.guild.id) in server["reply"]:
                    await ctx.send(embed=e)
                else:
                    await ctx.reply(embed=e, mention_author=False)
        if act == '-rem':
            if str(it) in usr["items"]:
                if not str(member.id) in usr["items"][str(it)]:
                    e = discord.Embed(
                        title=f'{err} Ошибка!',
                        description=f'У {member.mention} нет предмета "{it}"!',
                        color=err_color
                    )
                    if str(ctx.guild.id) in server["reply"]:
                        await ctx.send(embed=e)
                    else:
                        await ctx.reply(embed=e, mention_author=False)
                else:
                    del usr["items"][str(it)][str(member.id)]
                    with open('databases/users_settings/user_db.json', 'w') as f:
                        json.dump(usr, f) 
                    e = discord.Embed(
                        title=f'{tru} Успешно!',
                        description=f'Предмет "{str(it)}" изъят у {member.mention}!',
                        color=su_color
                    )
                    if str(ctx.guild.id) in server["reply"]:
                        await ctx.send(embed=e)
                    else:
                        await ctx.reply(embed=e, mention_author=False)
            else:
                e = discord.Embed(
                    title=f'{err} Ошибка!',
                    description=f'Предмета "{it}" нет в списке всех предметов!',
                    color=err_color
                )
                if str(ctx.guild.id) in server["reply"]:
                    await ctx.send(embed=e)
                else:
                    await ctx.reply(embed=e, mention_author=False)

    ###ECONOMY###
    @commands.command()
    async def money(
        self,
        ctx,
        type = None,
        value: int = None,
        member: discord.Member = None
    ):  
        with open('databases/economy_data/economy_db.json', 'r') as f:
            eco = json.load(f)
        with open('databases/server_settings/mass_db.json', 'r') as f:
            server = json.load(f)
        with open('databases/users_settings/user_db.json', 'r') as f:
            usr = json.load(f)
        err = discord.utils.get(self.Bot.emojis, name='cfalse')
        tru = discord.utils.get(self.Bot.emojis, name='ctrue')
        ### CHEKING
        if str(ctx.author.id) in usr["root"]:
            if not member == None:
                if not str(member.id) in eco["users"]["money"]:
                    eco["users"]["money"][str(member.id)] = 25
                if not str(member.id) in eco["users"]["bank"]:
                    eco["users"]["bank"][str(member.id)] = 25
                if not str(member.id) in eco["users"]["crypto"]["userbalance"]:
                    eco["users"]["crypto"]["userbalance"][str(member.id)] = 0
            else:
                pass
            ### CHEKING
            if type == None and value == None and member == None:
                e = discord.Embed(
                    title=f'{err} Вы не указали парметры:',
                    description='''> Действие 
> Сумма
> Пользователь

`!money <type> <value> <member>`''',
                    color=err_color
                )
                if str(ctx.guild.id) in server["reply"]:
                    await ctx.send(embed=e)
                else:
                    await ctx.reply(embed=e, mention_author=False)
            else:
                if type == '-add':
                    eco["users"]["money"][str(member.id)] += value
                    with open('databases/economy_data/economy_db.json', 'w') as f:
                        json.dump(eco, f)
                    e = discord.Embed(
                        title=f'{tru} Успешно!',
                        description=f'К балансу пользователя {member.mention} добавлено **{value}₽**.',
                        color=su_color
                    )
                    if str(ctx.guild.id) in server["reply"]:
                        await ctx.send(embed=e)
                    else:
                        await ctx.reply(embed=e, mention_author=False)
                if type == '-rem':
                    eco["users"]["money"][str(member.id)] -= value
                    with open('databases/economy_data/economy_db.json', 'w') as f:
                        json.dump(eco, f)
                    e = discord.Embed(
                        title=f'{tru} Успешно!',
                        description=f'С баланса пользователя {member.mention} было списано **{value}₽**.',
                        color=su_color
                    )
                    if str(ctx.guild.id) in server["reply"]:
                        await ctx.send(embed=e)
                    else:
                        await ctx.reply(embed=e, mention_author=False)
                if type == '-fix':
                    eco["users"]["money"][str(member.id)] = value
                    with open('databases/economy_data/economy_db.json', 'w') as f:
                        json.dump(eco, f)
                    e = discord.Embed(
                        title=f'{tru} Успешно!',
                        description=f'Баланс пользователя {member.mention} теперь равен **{value}₽**.',
                        color=su_color
                    )
                    if str(ctx.guild.id) in server["reply"]:
                        await ctx.send(embed=e)
                    else:
                        await ctx.reply(embed=e, mention_author=False)
        else:
            e = discord.Embed(
                title=f'{err} Отказано в доступе!',
                description=f'Получите **root** для управления этой командой.',
                color=err_color
            )
            if str(ctx.guild.id) in server["reply"]:
                await ctx.send(embed=e)
            else:
                await ctx.reply(embed=e, mention_author=False)

    @commands.command()
    @commands.is_owner()
    async def course(
        self,
        ctx,
        val: int
    ):
        with open('databases/economy_data/economy_db.json', 'r') as f:
            eco = json.load(f)
        with open('databases/server_settings/mass_db.json', 'r') as f:
            server = json.load(f)
        tru = discord.utils.get(self.Bot.emojis, name='ctrue')
        eco["users"]["crypto"]["cryptovalue"] = val
        with open('databases/economy_data/economy_db.json', 'w') as f:
            json.dump(eco, f)
        e = discord.Embed(
            title=f'{tru} Успешно!',
            description=f'Курс криптовалюты успешно изменен до **{val}₽** за единицу.',
            color=su_color
        )
        if str(ctx.guild.id) in server["reply"]:
            await ctx.send(embed=e)
        else:
            await ctx.reply(embed=e, mention_author=False)

    ###ElectiveVariableAcodeLundshufter (EVAL)
    @commands.command(
        aliases = ['e']
    )
    @commands.is_owner()
    async def eval(
        self, 
        ctx, 
        *, 
        code = None
        ):
        with open('databases/server_settings/mass_db.json', 'r') as f:
            server = json.load(f)
        with open('databases/users_settings/user_db.json', 'r') as f:
            usr = json.load(f)
        err = discord.utils.get(self.Bot.emojis, name='cfalse')
        tru = discord.utils.get(self.Bot.emojis, name='ctrue')
        wt = discord.utils.get(self.Bot.emojis, name='cnone')
        if str(ctx.author.id) in usr["root"]:
            if code == None:
                e = discord.Embed(
                    title=f'{wt} Вы не ввели параметр:',
                    description = '''> Код
                    
**Примечание:** 
    Словарь:
        Working bot vaiable: {`Bot`, bot`, self.client`, `self.Client`, `client`, `Client`}.
        "ctx" contains only `ctx`.''',
                    colour=null_color
                    )
                await ctx.reply(embed=e)
            else:
                start = time.perf_counter()
                language_specifiers = ["python", "py"]
                loops = 0
                while code.startswith("`"):
                    code = "".join(list(code)[1:])
                    loops += 1
                    if loops == 3:
                        loops = 0
                        break
                for language_specifier in language_specifiers:
                    if code.startswith(language_specifier):
                        code = code.lstrip(language_specifier)
                while code.endswith("`"):
                    code = "".join(list(code)[0:-1])
                    loops += 1
                    if loops == 3:
                        break
                code = "\n".join(f"    {i}" for i in code.splitlines())
                code = f"async def eval_expr():\n{code}"
                env = {
                    "Bot": self.Bot,
                    "bot": self.Bot,
                    "self.client": self.Bot,
                    "self.Client": self.Bot,
                    "client": self.Bot,
                    "Client": self.Bot,
                    "ctx": ctx
                }
                env.update(globals())
                end = time.perf_counter()
                try:
                    exec(code, env)
                    eval_expr = env["eval_expr"]
                    result = await eval_expr()
                    if result:
                        await ctx.reply(f'```py\n{result}```')
                    e = discord.Embed(
                        title=f'{tru} Работа программы завершена! Выполнено за: {round(((end - start) * 100), 3)} сек.',
                        description=f'''> **Ввод:**
```py\n{code}```
> **Вывод:**
```py\nКод выполнен успешно!```''',
                        color=null_color
                    )
                    e.set_footer(text=f'Вызвал: {ctx.author}')
                    await ctx.reply(embed=e)
                except Exception:
                    e = discord.Embed(
                        title=f'{err} Ошибка в ходе работы команды! На выполнение ушло: {round(((end - start) * 100), 3)} сек.',
                        description = f'''> **Ввод:**
```py\n{code}```
> **Вывод:**
```py\nПри выполнении кода возникли проблемы!```
> Full description (Traceback most recent calls):
```py\n{Exception}```''',
                        colour=null_color
                        )
                    e.set_footer(text=f'Вызвал: {ctx.author}')
                    await ctx.reply(embed=e)
                    return
        else:
            e = discord.Embed(
                title=f'{err} Отказано в доступе!',
                description=f'Получите **root** для управления этой командой.',
                color=err_color
            )
            if str(ctx.guild.id) in server["reply"]:
                await ctx.send(embed=e)
            else:
                await ctx.reply(embed=e, mention_author=False)

def setup (Bot):
    Bot.add_cog(root(Bot))
