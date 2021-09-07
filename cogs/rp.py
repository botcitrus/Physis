  
import discord
from discord.ext import commands
import random

base_color=0xACE1AF

class RP(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def паспорт(self, ctx):
        imya = random.choice(['Гавриил' ,'Галактион' ,'Геласий' ,'Геннадий' ,'Георгий' ,'Герасим' ,'Герман' ,'Германн' ,'Глеб' ,'Гордей' ,'Григорий' ,'Тарас' ,'Тимофей' ,'Тимур' ,'Тит' ,'Тихон' ,'Трифон' ,'Трофим' ,'Фаддей' ,'Фёдор' ,'Федосей' ,'Федот' ,'Феликс' ,'Феоктист' ,'Филимон' ,'Филипп' ,'Фирс' ,'Фока' ,'Фома' ,'Фотий' ,'Фрол'])
        family = random.choice(['Лазарев', 'Медведев', 'Ершов', 'Никитин', 'Соболев' ,'Рябов', 'Поляков', 'Цветков', 'Данилов', 'Жуков', 'Фролов', 'Журавлёв', 'Николаев', 'Крылов', 'Максимов', 'Сидоров', 'Осипов', 'Дорофeeв', 'Егоров', 'Матвеев', 'Бобров', 'Дмитриев', 'Калинин', 'Анисимов', 'Петухов', 'Антонов', 'Тимофеев', 'Никифоров', 'Веселов', 'Филиппов', 'Марков', 'Большаков', 'Суханов', 'Миронов', 'Ширяев', 'Александров', 'Коновалов', 'Шестаков', 'Казаков', 'Ефимов', 'Денисов', 'Громов', 'Фомин', 'Давыдов', 'Мельников', 'Щербаков', 'Блинов', 'Колесников'])
        otchestvo = random.choice(['Ааронович' ,'Абрамович' ,'Августович' ,'Авдеевич' ,'Аверьянович' ,'Адамович' ,'Адрианович' ,'Акимович' ,'Аксёнович' ,'Александрович' ,'Алексеевич' ,'Анатольевич' ,'Андреевич' ,'Андроникович' ,'Анисимович' ,'Антипович' ,'Антонович' ,'Ануфриевич' ,'Аркадьевич' ,'Арсенович' ,'Арсеньевич' ,'Артёмович' ,'Артемьевич' ,'Артурович' ,'Архипович' ,'Афанасьевич' ,'Евгеньеви' ,'Евграфович' ,'Евдокимович' ,'Евсеевич' ,'Егорович' ,'Елизарович' ,'Елисеевич' ,'Емельянович' ,'Еремеевич' ,'Ермилови' ,'Ермолаевич' ,'Ерофеевич' ,'Ефимович' ,'Ефимьевич' ,'Ефремович' ,'Ефстафьевич'])
        s = random.choice(['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31', ])
        r = random.choice(['1','2','3','4','5','6','7','8','9','10','11','12'])
        t = random.choice(['1974','1975','1976','1977','1978','1979','1980','1981','1982','1983','1984','1985', '1986', '1987', '1988', '1989', '1990', '1991' ,'1992'])
        ylitsya = random.choice(['Ул. Лызина 89', 'Ул. Черепахова', 'Ул. Школьная 25', 'Ул. Ленина 19'])
        u = random.choice([111, 121, 131, 141, 151, 161, 171, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65])
        y = random.choice([1111, 12, 13, 14, 15, 16, 17, 1811, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65])
        q = random.choice([11111, 12111, 13111, 14111, 15111, 16111, 17111, 18111, 19111, 20111, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65])
        emb = discord.Embed(title = 'Паспортные Данные:', description =f'Фамилия: {family}\nИмя: {imya}\nОтчество: {otchestvo}\nДата Рождения: {s}.{r}.{t}\nСерия Паспорта: {u}.{y}.{q}', color=0XFF0000)
        emb.set_footer(text='Данная команда создана по фану', icon_url=ctx.author.avatar_url)
        await ctx.send(embed = emb)
	
    @commands.command()
    async def actions(self, ctx):
        emb = discord.Embed(title='<a:pro:871662029025443892> Действия', color = 0x00FFFF)
        emb.set_author(name= ctx.author.name, icon_url = ctx.author.avatar_url)
        emb.add_field( name = '`{}oбнять`'.format( "." ), value = 'Обнять.')
        emb.add_field( name = '`{}пощекотать`'.format( "." ), value = 'Пощекотать.')
        emb.add_field( name = '`{}прижать`'.format( "." ), value = 'Прижаться.')
        emb.add_field( name = '`{}поцеловать`'.format( "." ), value = 'Поцеловать.')
        emb.add_field( name = '`{}гладить`'.format( "." ), value = 'Гладить.')
        emb.add_field( name = '`{}пощечина`'.format( "." ), value = 'Пощечина.')
        emb.add_field( name = '`{}подмигнуть`'.format( "." ), value = 'Подмигнуть.')
        emb.add_field( name = '`{}чай`'.format( "." ), value = 'Пить чай.')
        emb.set_author(name=ctx.author.name, icon_url = ctx.author.avatar_url)
        await ctx.send(embed=emb)
	
    @commands.command()
    async def прижать(self, ctx, member: discord.Member = None):
        embed = discord.Embed(color = 0x00FFFF)
        if member != None:
            embed.description = f"{ctx.author.mention} прижимается к {member.mention}."
        else:
            embed.description = f"{ctx.author.mention} прижимается к кому-то..."
        embed.set_image(url = 'https://acegif.com/wp-content/uploads/hugs-30.gif') 
        await ctx.send(embed = embed)

    @commands.command()
    async def удар(self, ctx, member: discord.Member = None):
        slappp = ['https://i.gifer.com/79zo.gif', 'https://safebooru.org/images/1882/605143df221803e99f3b5423f1df4c8b76bd8ae9.gif?1964756', 'https://i.kym-cdn.com/photos/images/original/001/040/951/73e.gif']
        embed = discord.Embed(color = 0x00FFFF)
        if member != None:
            embed.description = f"{ctx.author.mention} дал леща {member.mention}."
        else:
            embed.description = f"{ctx.author.mention} дал леща кому-то..."
        embed.set_image(url = random.choice(slappp)) 
        await ctx.send(embed = embed)

    @commands.command()
    async def поцеловать(self, ctx, member: discord.Member = None):
        kisss = ['https://data.whicdn.com/images/294084710/original.gif', 'https://im0-tub-ru.yandex.net/i?id=891bd2b6228afa51bd76bc2c61050a17&n=13']
        embed = discord.Embed(color = 0x00FFFF)
        if member != None:
            embed.description = f"{ctx.author.mention} целует {member.mention}."
        else:
            embed.description = f"{ctx.author.mention} целует кого-то..."
        embed.set_image(url = random.choice(kisss)) 
        await ctx.send(embed = embed)
	
    @commands.command()
    async def обнять(self, ctx, member: discord.Member = None):
        embed = discord.Embed(color = 0x00FFFF)
        if member != None:
            embed.description = f"{ctx.author.mention} обнимает {member.mention}."
        else:
            embed.description = f"{ctx.author.mention} обнимает кого-то..."
        embed.set_image(url = 'http://pristor.ru/wp-content/uploads/2018/07/%D0%9F%D1%80%D0%B8%D0%BA%D0%BE%D0%BB%D1%8C%D0%BD%D1%8B%D0%B5-%D0%B8-%D0%BA%D1%80%D0%B0%D1%81%D0%B8%D0%B2%D1%8B%D0%B5-%D0%BE%D1%82%D0%BA%D1%80%D1%8B%D1%82%D0%BA%D0%B8-%D0%B3%D0%B8%D1%84%D0%BA%D0%B8-%D0%B4%D0%BB%D1%8F-%D0%B4%D1%80%D1%83%D0%B3%D0%B0-GIF-%D0%B0%D0%BD%D0%B8%D0%BC%D0%B0%D1%86%D0%B8%D1%8F-2.gif') 
        await ctx.send(embed = embed)
	
    @commands.command()
    async def гладить(self, ctx, member: discord.Member = None):
        embed = discord.Embed(color = 0x00FFFF)
        if member != None:
            embed.description = f"{ctx.author.mention} гладит {member.mention}."
        else:
            embed.description = f"{ctx.author.mention} гладит кого-то..."
        embed.set_image(url = 'https://99px.ru/sstorage/86/2017/09/10509171755521838.gif') 
        await ctx.send(embed = embed)
	
    @commands.command()
    async def подмигнуть(self, ctx, member: discord.Member = None):
        embed = discord.Embed(color = 0x00FFFF)
        if member != None:
            embed.description = f"{ctx.author.mention} подмигивает {member.mention}."
        else:
            embed.description = f"{ctx.author.mention} подмигивает кому-то..."
        embed.set_image(url = 'https://media1.tenor.com/images/d8df012e313209ceb60090608b3fff12/tenor.gif?itemid=14737099') 
        await ctx.send(embed = embed)
	
    @commands.command()
    async def шекотать(self, ctx, member: discord.Member = None):
        tickkle = ['https://i.gifer.com/KVjQ.gif', 'https://i.gifer.com/O4QR.gif', 'https://66.media.tumblr.com/e6d1a1cd2499e37f14118a75d5e36da4/tumblr_og7p24fa3R1vpbklao6_500.gifv']
        embed = discord.Embed(color = 0x00FFFF)
        if member != None:
            embed.description = f"{ctx.author.mention} щекотит пятки {member.mention}."
        else:
            embed.description = f"{ctx.author.mention} щекотит кому-то пятки..."
        embed.set_image(url = random.choice(tickkle)) 
        await ctx.send(embed = embed)
	
    @commands.command()
    async def чай(self, ctx, member: discord.Member = None):
        embed = discord.Embed(color = 0x00FFFF)
        if member != None:
            embed.description = f"{ctx.author.mention} пьёт чай с {member.mention}."
        else:
            embed.description = f"{ctx.author.mention} пьёт чай с кем-то..."
        embed.set_image(url = 'https://peopletalk.ru/wp-content/uploads/2016/09/tumblr_ldk69syJ0y1qbjpavo1_500.gif') 
        await ctx.send(embed = embed)


def setup(client):
	client.add_cog(RP(client))