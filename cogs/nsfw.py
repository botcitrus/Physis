import discord
from discord.ext import commands
import nekos
import random

Arguments = ['feet', 'yuri', 'trap', 'futanari', 'hololewd', 'lewdkemo', 'solog', 'feetg', 'cum', 'erokemo', 'les', 'wallpaper', 'lewdk', 'ngif', 'tickle', 'lewd', 'feed', 'gecg', 'eroyuri', 'eron', 'cum_jpg', 'bj', 'nsfw_neko_gif', 'solo', 'kemonomimi', 'nsfw_avatar', 'gasm', 'poke', 'anal', 'slap', 'hentai', 'avatar', 'erofeet', 'holo', 'keta', 'blowjob', 'pussy', 'tits', 'holoero', 'lizard', 'pussy_jpg', 'pwankg', 'classic', 'kuni', 'waifu', 'pat', '8ball', 'kiss', 'femdom', 'neko', 'spank', 'cuddle', 'erok', 'fox_girl', 'boobs', 'random_hentai_gif', 'smallboobs', 'hug', 'ero', 'smug', 'goose', 'baka', 'woof']
def is_nsfw():
    async def predicate(ctx):
        return ctx.channel.is_nsfw()
    return commands.check(predicate)
queue = []
base_color=0xACE1AF

class Sex(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @is_nsfw()
    async def feet(self, ctx):
        emb = discord.Embed(color=0xebebeb)
        emb.set_image(url= nekos.img('feet'))
        emb.set_author(name= ctx.author.name, icon_url = ctx.author.avatar_url)
        await ctx.send(embed=emb)
	
    @commands.command()
    @is_nsfw()
    async def trap(self, ctx):
        emb = discord.Embed(color=0xebebeb)
        emb.set_image(url=nekos.img('trap'))
        emb.set_author(name=ctx.author.name, icon_url = ctx.author.avatar_url)
        await ctx.send(embed=emb)

    @commands.command()
    @is_nsfw()
    async def futanari(self, ctx):
        emb = discord.Embed(color=0xebebeb)
        emb.set_image(url=nekos.img('futanari'))
        emb.set_author(name=ctx.author.name, icon_url = ctx.author.avatar_url)
        await ctx.send(embed=emb)

    @commands.command()
    @is_nsfw()
    async def lewdkemo(self, ctx):
        emb = discord.Embed(color=0xebebeb)
        emb.set_image(url=nekos.img('lewdkemo'))
        emb.set_author(name=ctx.author.name, icon_url = ctx.author.avatar_url)
        await ctx.send(embed=emb)

    @commands.command()
    @is_nsfw()
    async def solog(self, ctx):
        emb = discord.Embed(color=0xebebeb)
        emb.set_image(url=nekos.img('solog'))
        emb.set_author(name=ctx.author.name, icon_url = ctx.author.avatar_url)
        await ctx.send(embed=emb)

    @commands.command()
    @is_nsfw()
    async def erokemo(self, ctx):
        emb = discord.Embed(color=0xebebeb)
        emb.set_image(url=nekos.img('erokemo'))
        emb.set_author(name=ctx.author.name, icon_url = ctx.author.avatar_url)
        await ctx.send(embed=emb)

    @commands.command()
    @is_nsfw()
    async def les(self, ctx):
        emb = discord.Embed(color=0xebebeb)
        emb.set_image(url=nekos.img('les'))
        emb.set_author(name=ctx.author.name, icon_url = ctx.author.avatar_url)
        await ctx.send(embed=emb)

    @commands.command()
    @is_nsfw()
    async def wallpaper(self, ctx):
        emb = discord.Embed(color=0xebebeb)
        emb.set_image(url=nekos.img('wallpaper'))
        emb.set_author(name=ctx.author.name, icon_url = ctx.author.avatar_url)
        await ctx.send(embed=emb)

    @commands.command()
    @is_nsfw()
    async def lewdk(self, ctx):
        emb = discord.Embed(color=0xebebeb)
        emb.set_image(url=nekos.img('lewdk'))
        emb.set_author(name=ctx.author.name, icon_url = ctx.author.avatar_url)
        await ctx.send(embed=emb)

    @commands.command()
    @is_nsfw()
    async def ngif(self, ctx):
        emb = discord.Embed(color=0xebebeb)
        emb.set_image(url=nekos.img('ngif'))
        emb.set_author(name=ctx.author.name, icon_url = ctx.author.avatar_url)
        await ctx.send(embed=emb)

    @commands.command()
    @is_nsfw()
    async def щекотать(self, ctx):
        emb = discord.Embed(color=0xebebeb)
        emb.set_image(url=nekos.img('tickle'))
        emb.set_author(name=ctx.author.name, icon_url = ctx.author.avatar_url)
        await ctx.send(embed=emb)

    @commands.command()
    @is_nsfw()
    async def lewd(self, ctx):
        emb = discord.Embed(color=0xebebeb)
        emb.set_image(url=nekos.img('lewd'))
        emb.set_author(name=ctx.author.name, icon_url = ctx.author.avatar_url)
        await ctx.send(embed=emb)

    @commands.command()
    @is_nsfw()
    async def feed(self, ctx):
        emb = discord.Embed(color=0xebebeb)
        emb.set_image(url=nekos.img('feed'))
        emb.set_author(name=ctx.author.name, icon_url = ctx.author.avatar_url)
        await ctx.send(embed=emb)

    @commands.command()
    @is_nsfw()
    async def gecg(self, ctx):
        emb = discord.Embed(color=0xebebeb)
        emb.set_image(url=nekos.img('gecg'))
        emb.set_author(name=ctx.author.name, icon_url = ctx.author.avatar_url)
        await ctx.send(embed=emb)

    @commands.command()
    @is_nsfw()
    async def avatar(self, ctx):
        emb = discord.Embed(color=0xebebeb)
        emb.set_image(url=nekos.img('avatar'))
        emb.set_author(name=ctx.author.name, icon_url = ctx.author.avatar_url)
        await ctx.send(embed=emb)

    @commands.command()
    @is_nsfw()
    async def boobs(self, ctx):
        emb = discord.Embed(color=0xebebeb)
        emb.set_image(url=nekos.img('boobs'))
        emb.set_author(name=ctx.author.name, icon_url = ctx.author.avatar_url)
        await ctx.send(embed=emb)

    @commands.command()
    @is_nsfw()
    async def kuni(self, ctx):
        emb = discord.Embed(color=0xebebeb)
        emb.set_image(url=nekos.img('kuni'))
        emb.set_author(name=ctx.author.name, icon_url = ctx.author.avatar_url)
        await ctx.send(embed=emb)


def setup(client):
	client.add_cog(Sex(client))