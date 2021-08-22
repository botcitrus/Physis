import discord
from discord.ext import commands
from Cybernator import Paginator
from datetime import datetime
import time
import asyncio
import json
import psutil

base_color=0x3498db
su_color=0x2ecc71
err_color=0xe74c3c

class docs_and_tech(commands.Cog):
    def __init__(self, Bot):
        self.Bot = Bot

    @commands.command(
        aliases=['хелп', 'помощь']
    )
    async def help(
        self,
        ctx
    ):
        with open('databases/server_settings/mass_db.json', 'r') as f:
            server = json.load(f)
        emb = discord.Embed(
           title=f'Самая важная информация про {self.Bot.user}.',
           color=base_color
           )
        emb.add_field(
            name='Информация', 
            value='`!хелп` `!команды` `!сервер` `!профиль` `!о_себе` `!бот`',
            inline=False
            )
        emb.add_field(
            name='Модерация', 
            value='`!кик` `!бан` `!удалить` `!роль` `!рроль`',
            inline=False
            )
        emb.add_field(
            name='Экономика', 
            value='''`!бонус` `!работа` `!премиум` `!баланс` `!перевод`, 
`!депозит` `!снять` `!кено` `!крипто` `!крипто_купить` 
`!крипто_продать`''',
            inline=False
            )
        emb.add_field(
            name='Утилиты',
            value='`!центр` `!ответы`',
            inline=False
            )
        emb.add_field(
            name='Фан',
            value='`!монетка` `!пёсель` `!кот`',
            inline=False
            )
        emb.add_field(
            name='Возникла проблема?',
            value='''[ТехПоддержка](https://discord.gg/bF4SGguHxC)''',
            inline=True
            )
        emb.add_field(
            name=f'Пригласить бота',
            value='''[Ссылка для приглашения](https://discord.com/oauth2/authorize?client_id=842327791806840832&permissions=8&scope=bot)''',
            inline=True
            )
        emb.add_field(
            name=f'Официальный сервер', 
            value='''[Ссылка на сервер](https://discord.gg/dVbPMUKFnh)''',
            inline=True
            )
        emb.set_thumbnail(url="https://wmpics.pics/di-SBCO.png")
        emb.set_footer(
            text="By DarkJoij#3009", 
            icon_url='https://wmpics.pics/di-YEE6.jpg'
            )
        if str(ctx.guild.id) in server["reply"]:
            await ctx.send(embed=emb)
        else:
            await ctx.reply(embed=emb, mention_author=False)
    
    @commands.command(
        aliases = ['сервер', 'server_info', 'сервер_инфо', 'serv', 'серв']
        )
    async def server(
        self, 
        ctx
        ):
        with open('databases/server_settings/mass_db.json', 'r') as f:
            server = json.load(f)
        bot = discord.utils.get(self.Bot.emojis, name='bot')
        peop = discord.utils.get(self.Bot.emojis, name='users_total')
        peopoff = discord.utils.get(self.Bot.emojis, name='offline')
        peopon = discord.utils.get(self.Bot.emojis, name='online1')
        peopsl = discord.utils.get(self.Bot.emojis, name='idle')
        peopdnd = discord.utils.get(self.Bot.emojis, name='dnd')
        users = discord.utils.get(self.Bot.emojis, name='user')
        cat = discord.utils.get(self.Bot.emojis, name='settings')
        chan = discord.utils.get(self.Bot.emojis, name='category')
        reash = discord.utils.get(self.Bot.emojis, name='channel')
        voice = discord.utils.get(self.Bot.emojis, name='voice_channels')
        roles = discord.utils.get(self.Bot.emojis, name='rules')
        bstlvl = discord.utils.get(self.Bot.emojis, name='multiboosting')
        emb = discord.Embed(description=f'''**Основное:**
:link: ID: **{ctx.guild.id}**
{roles} Всего ролей: **{len(ctx.guild.roles) - 1}**
{bstlvl} Бустов: **{ctx.guild.premium_subscription_count}**''',
            color=base_color,
            timestamp=datetime.utcnow()
            )
        emb.set_author(
            name=f'Информация о сервере {ctx.guild.name}.',
            url = 'https://discord.gg/dVbPMUKFnh', 
            )
        emb.set_thumbnail(url=ctx.guild.icon_url)
        emb.add_field(
            name='Информация о учатниках:', 
            value=f'''{users} Всего: **{ctx.guild.member_count}**
{peopon} Онлайн: **{sum(member.status==discord.Status.online for member in ctx.guild.members)}**
{peopoff} Офлайн: **{sum(member.status==discord.Status.offline for member in ctx.guild.members)}**
{peopsl} Не активен: **{sum(member.status==discord.Status.idle for member in ctx.guild.members)}**
{peopdnd} Не беспокоить: **{sum(member.status==discord.Status.dnd for member in ctx.guild.members)}**
{peop} Пользователей: **{sum(not member.bot for member in ctx.guild.members)}**
{bot} Ботов: **{sum(member.bot for member in ctx.guild.members)}**''', inline=True)
        emb.add_field(
            name='Информация о каналах:', 
            value=f'''{cat} Категорий: **{len(ctx.guild.categories)}**
{chan} Каналов: **{len(ctx.guild.channels) - (len(ctx.guild.categories) + 1)}**
{reash} Текстовых: **{len(ctx.guild.text_channels)}**
{voice} Голосовых: **{len(ctx.guild.voice_channels)}**''', inline=True)
        emb.set_footer(
            text='Владелец сервера: {}'.format(ctx.guild.owner),
            icon_url=ctx.guild.owner.avatar_url
            )
        if str(ctx.guild.id) in server["reply"]:
            await ctx.send(embed=emb)
        else:
            await ctx.reply(embed=emb, mention_author=False)

    @commands.command(
        aliases = ['профиль', 'юзер', 'p', 'ю', 'prof', 'проф']
    )
    async def profile(
        self,
        ctx,
        member: discord.Member = None
    ):
        if member == None:
            member = ctx.author
        with open('databases/server_settings/mass_db.json', 'r') as f:
            server = json.load(f)
        with open('databases/users_settings/user_db.json', 'r') as f:
            usr = json.load(f)
        with open('databases/economy_data/economy_db.json', 'r') as f:
            econ = json.load(f)
        date_format = "%b %d, %Y в %I:%M %p"
        bnk = discord.utils.get(self.Bot.emojis, name='bank')
        alphasup = discord.utils.get(self.Bot.emojis, name='earlysupporter')
        uni = discord.utils.get(self.Bot.emojis, name='unicoin')
        prem = discord.utils.get(self.Bot.emojis, name='hypesquad')
        peopon = discord.utils.get(self.Bot.emojis, name='online1')
        peopdnd = discord.utils.get(self.Bot.emojis, name='dnd')
        members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
        if not str(member.id) in econ["users"]["money"]:
            econ["users"]["money"][str(member.id)] = 25
        if not str(member.id) in econ["users"]["bank"]:
            econ["users"]["bank"][str(member.id)] = 25
        if not str(member.id) in econ["users"]["crypto"]["userbalance"]:
            econ["users"]["crypto"]["userbalance"][str(member.id)] = 0
        with open('databases/economy_data/economy_db.json', 'w') as f:
            json.dump(econ, f)
        emb = discord.Embed(
            color=base_color,
            timestamp=datetime.utcnow()
            )
        emb.set_author(
            name=f'Информация о пользователе {member}', 
            url='https://discord.gg/dVbPMUKFnh', 
            icon_url=member.avatar_url
            )
        if not str(member.id) in usr["bio"]: # 0 1
            emb.add_field(
                name="О себе:", 
                value='Пользователь не добавил информации о себе. Изменить информацию "о себе" можно командой **!о_себе**.', 
                inline=False
                )
        else:
            emb.add_field(
                name="О себе:", 
                value=usr["bio"][str(member.id)], 
                inline=False
                )
        if member.status==discord.Status.offline:
            emb.add_field( # 1 2
                name="Статус",
                value=f"{discord.utils.get(self.Bot.emojis, name='offline')} Не в сети", 
            )
        elif member.status==discord.Status.online:
            emb.add_field( # 1 2
                name="Статус",
                value=f"{discord.utils.get(self.Bot.emojis, name='online1')} В сети", 
            )
        elif member.status==discord.Status.idle:
            emb.add_field( # 1 2
                name="Статус",
                value=f"{discord.utils.get(self.Bot.emojis, name='idle')} Не активен", 
            )
        elif member.status==discord.Status.dnd:
            emb.add_field( # 1 2
                name="Статус",
                value=f"{discord.utils.get(self.Bot.emojis, name='dnd')} Не беспокоить", 
            )
        if member.activity == None:
            emb.add_field( # 1 3
                name="Пользовательский статус",
                value="Не доступен",
            )
        else:
            emb.add_field( # 1 3
                name="Пользовательский статус",
                value=member.activity.name,
            )
        emb.add_field(# 2 3
            name="Высшая роль", 
            value=member.top_role.mention, 
            )
        emb.add_field( # 2 1 
            name="Аккаунт создан", 
            value=member.created_at.strftime(date_format), 
            )
        emb.add_field( # 2 1 
            name="Присоедился к серверу", 
            value=member.joined_at.strftime(date_format), 
            )
        emb.add_field(# 2 2
            name="На сервере по счёту", 
            value=str(members.index(member) + 1), 
            )
        emb.add_field( # 3 1
            name="Экономика",
             value=f''':money_with_wings: Баланс: **{econ["users"]["money"][str(member.id)]}₽**
{bnk} В банке: **{econ["users"]["bank"][str(member.id)]}₽**
:coin: Крипто-баланс: **{econ["users"]["crypto"]["userbalance"][str(member.id)]}EC**''', 
             )
        emb.add_field(
            name='Подробная информация',
            value=f'''**Серверное имя:** {member.display_name}
**Тег:** {member}
**ID:** {member.id}'''
            )
        if str(member.id) in usr["root"]:
            emb.add_field(
                name='Раширенные права',
                value=f'{peopon} ROOT-доступ.'
                )
        else:
            emb.add_field(
                name='Раширенные права',
                value=f'{peopdnd} Отсутсвуют.'
                )
        emb2 = discord.Embed(
            color=base_color,
            timestamp=datetime.utcnow()
            )
        emb2.set_author(
            name=f'Личные значки пользователя {member}', 
            url='https://discord.gg/dVbPMUKFnh', 
            icon_url=member.avatar_url
            )
        if not str(member.id) in usr["items"]['alphasupporter'] and not str(member.id) in usr["items"]['premium'] and not str(member.id) in usr["items"]['haknow']:
            emb2.add_field(
                name=f'Нет отличительных значков.',
                value='Присоединяйтесь к [официальному серверу бота](https://discord.gg/dVbPMUKFnh) узнать как получать значки.',
                inline=False
            )
        if str(member.id) in usr["items"]['alphasupporter']:
            emb2.add_field(
                name=f'{alphasup} | Альфа-тестировщик бота',
                value='''╰ Член команды тестировки бота. Принимал участие в самых первых тестах и внёс огромный вклад в развитие бота. 
__Данный значок получить более никак нельзя__.''',
                inline=False
            )
        else:
            pass
        if str(member.id) in usr["items"]["premium"]:
            emb2.add_field(
                name=f'{prem} | Премиум пользователь',
                value='''╰ __В данный момент значок находится в бета тесте__.
*Поистине могучий)*.''',
                inline=False
            )
        else:
            pass
        if str(member.id) in usr["items"]["haknow"]:
            emb2.add_field(
                name=f'{uni} | Просвещённый',
                value='╰ Выдан за секретную информацию. Ходят слухи, что еще можно получить этот уникальный предмет...',
                inline=False
            )
        else:
            pass
        embeds = [emb, emb2]
        if str(ctx.guild.id) in server["reply"]:
            message = await ctx.send(embed=emb)
        else:
            message = await ctx.reply(embed=emb, mention_author=False)
        page = Paginator(self.Bot, message, only=ctx.author, use_more=False, use_exit=True, footer=False, embeds=embeds) 
        await page.start()

    
    @commands.command(
        aliases=['BIO', 'о_себе', 'О_СЕБЕ', 'био', 'БИО']
    )
    async def bio(
        self,
        ctx,
        *,
        biotxt = None
    ):
        with open('databases/server_settings/mass_db.json', 'r') as f:
            server = json.load(f)
        err = discord.utils.get(self.Bot.emojis, name='cfalse')
        tru = discord.utils.get(self.Bot.emojis, name='ctrue')
        with open('databases/users_settings/user_db.json', 'r') as f:
            usr = json.load(f)
        if biotxt == None:
            embed = discord.Embed(
                title=f'{err} Вы не указали параметр:',
                description = "> Текст",
                colour=err_color
                )
            if str(ctx.guild.id) in server["reply"]:
                await ctx.send(embed=embed)
            else:
                await ctx.reply(embed=embed, mention_author=False)
        elif len(biotxt) > 200:
            embed = discord.Embed(
                title=f'{err} Ошибка!',
                description = "Вы ввели слишком большой текст. Вы можете вводить текст размером до 200 символов",
                colour=err_color
                )
            if str(ctx.guild.id) in server["reply"]:
                await ctx.send(embed=embed)
            else:
                await ctx.reply(embed=embed, mention_author=False)
        elif biotxt == 'удалить' or biotxt == 'delete':
            if not str(ctx.author.id) in usr["bio"]:
                embed = discord.Embed(
                title=f'{err} Ошибка!',
                description = 'Ваше поле "о себе" не заполнено. Вы не можете удалить эти сведения.',
                colour=err_color
                )
                if str(ctx.guild.id) in server["reply"]:
                    await ctx.send(embed=embed)
                else:
                    await ctx.reply(embed=embed, mention_author=False)
            else:
                del usr["bio"][str(ctx.author.id)]
                with open('databases/users_settings/user_db.json', 'w') as f:
                    json.dump(usr, f)
                embed = discord.Embed(
                    title=f'{tru} Успешно!',
                    description = 'Информация "о себе" сброшена.',
                    colour=su_color
                    )
                if str(ctx.guild.id) in server["reply"]:
                    await ctx.send(embed=embed)
                else:
                    await ctx.reply(embed=embed, mention_author=False)
        else:
            usr["bio"][str(ctx.author.id)] = f'{biotxt}'
            with open('databases/users_settings/user_db.json', 'w') as f:
                json.dump(usr, f)
            embed = discord.Embed(
                title=f'{tru} Успешно!',
                description = f'Информация "о себе" изменена на *{biotxt}*',
                colour=su_color
                )
            if str(ctx.guild.id) in server["reply"]:
                await ctx.send(embed=embed)
            else:
                await ctx.reply(embed=embed, mention_author=False)
            
    @commands.command(
        aliases = ['eagle', 'botinfo', 'bot_info', 'бот', 'ботинфо', 'бот_инфо', 'сисинфо', ]
    )
    async def bot(
        self,
        ctx
        ):
        with open('databases/server_settings/mass_db.json', 'r') as f:
            server = json.load(f)
        wt = discord.utils.get(self.Bot.emojis, name='cnone')
        ld = discord.utils.get(self.Bot.emojis, name='loading2')
        start = time.perf_counter()
        if str(ctx.guild.id) in server["reply"]:
            message = await ctx.send(embed = discord.Embed(title=f'{ld} Пожалуйста подождите', description='Идет сбор и подсчёт информации...', color=base_color))
        else:
            message = await ctx.send(embed = discord.Embed(title=f'{ld} Пожалуйста подождите', description='Идет сбор и подсчёт информации...', color=base_color), mention_author=False)
        end = time.perf_counter()
        duration = (end - start) * 1000
        embed = discord.Embed(
            title=f"{wt} Расширенная информация про {self.Bot.user}",
            color=base_color
        )
        embed.set_thumbnail(url="https://wmpics.pics/di-SBCO.png")
        embed.add_field(
            name="ЦП", 
            value=f"> {psutil.cpu_percent(interval=None)}%",
            )
        embed.add_field(
            name="ОП", 
            value=f"> {psutil.virtual_memory()[2]}%",
        )
        embed.add_field(
            name="ОС", 
            value=f'> Linux',
        )
        embed.add_field(
            name="Пинг (ОВДО)",
            value=f"> {round(duration)}мс",
            )
        embed.add_field(
            name="Пинг (ответ)",
            value=f"> {round(self.Bot.latency * 1000)}мс",
            )
        embed.add_field(
            name="Номер пака", 
            value=f'> num' 
        )
        embed.add_field(
            name="Библиотека", 
            value=f'''> Discord.py 
v.{discord.__version__}'''
        )
        embed.add_field(
            name="ЯП", 
            value='''> Python 
> v.num'''
        )
        embed.add_field(
            name="Сборка", 
            value='''> num'''
        )
        embed.add_field(
            name="Серверов", 
            value=f'> {len(self.Bot.guilds)}'
        )
        embed.add_field(
            name="Пользователей", 
            value=f'> {len(self.Bot.users)}'
        )
        embed.add_field(
            name="Команд", 
            value=f'> num'
        )
        embed.set_footer(
            text = f'Запросил: {ctx.author}', 
            icon_url = ctx.author.avatar_url
            )
        await asyncio.sleep(2)
        await message.edit(embed=embed)

    @commands.command(
        aliases = ['юникоин']
    )
    async def unicoin(
        self,
        ctx
    ):
        member=ctx.author
        with open('databases/users_settings/user_db.json', 'r') as f:
            usr = json.load(f)
        tru = discord.utils.get(self.Bot.emojis, name='ctrue')
        if not str(ctx.author.id) in usr["items"]["haknow"]:
            usr["items"]["haknow"][str(ctx.author.id)] = True
            with open('databases/users_settings/user_db.json', 'w') as f:
                json.dump(usr, f)
            embed = discord.Embed(
                title=f'{tru} Успешно!',
                description = f'Секретный персональный значок "Просвещённый" активирован.',
                colour=su_color
                )
            await member.send(embed=embed)
        else:
            pass

    @commands.command(
        aliases = ['команды', 'список_команд', 'списоккоманд']
    )
    async def commands(
        self,
        ctx
    ):
        with open('databases/server_settings/mass_db.json', 'r') as f:
            server = json.load(f)
        emb1 = discord.Embed(
           title=f'Список команд | Категория Инфо',
           description='''**!хелп**: `Нет аргументов`
    Показывает самую нужную о боте.
**!команды**: `Нет аргументов`
    Вызывает это сообщение.
**!сервер**: `Нет аргуметов`
    Показывает сводку о сервере, на котором была вызвана команда.
**!профиль**: `!профиль <@юзер/ничего (юзером будет считаться автор)>`
    Показывает личный профиль и информацию о пользователе.
**!о_себе**: `!о_себе <текст/удалить>`
    Изменит или удалит информацию в поле "о себе".
**!бот**: `Нет аргументов`
    Покажет техническую информацию.''',
           color=base_color
           )
        emb2 = discord.Embed(
           title=f'Список команд | Категория Модерация',
           description=discord.utils.get(self.Bot.emojis, name='loading2'),
           color=base_color
           )
        embeds = [emb1, emb2]
        if str(ctx.guild.id) in server["reply"]:
            message = await ctx.send(embed=emb1)
        else:
            message = await ctx.reply(embed=emb1, mention_author=False)
        page = Paginator(self.Bot, message, only=ctx.author, use_more=False, use_exit=True, embeds=embeds) 
        await page.start()

def setup (Bot):
    Bot.add_cog(docs_and_tech(Bot))
