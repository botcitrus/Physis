import discord
from discord.ext import commands
import nekos
import random

base_color=0xACE1AF

class FUNK(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    async def плюс(self, ctx, *nums):
        operation = " + ".join(nums)
        emb = discord.Embed(description = f"<a:pro:871662029025443892> получилось {operation} = {eval(operation)} ")
        emb.set_author(name=ctx.author.name, icon_url = ctx.author.avatar_url)
        await ctx.send(embed=emb)

    @commands.command() 
    async def минус(self, ctx, *nums): 
        operation = " - ".join(nums)
        emb = discord.Embed(description = f"<a:pro:871662029025443892> получилось {operation} = {eval(operation)} ")
        emb.set_author(name=ctx.author.name, icon_url = ctx.author.avatar_url)
        await ctx.send(embed=emb)

    @commands.command() 
    async def умножить(self, ctx, *nums): 
        operation = " * ".join(nums)
        emb = discord.Embed(description = f"<a:pro:871662029025443892> получилось {operation} = {eval(operation)} ")
        emb.set_author(name=ctx.author.name, icon_url = ctx.author.avatar_url)
        await ctx.send(embed=emb)

    @commands.command() 
    async def разделить(self, ctx, *nums): 
        operation = " / ".join(nums)
        emb = discord.Embed(description = f"<a:pro:871662029025443892> получилось {operation} = {eval(operation)} ")
        emb.set_author(name=ctx.author.name, icon_url = ctx.author.avatar_url)
        await ctx.send(embed=emb)
	
    @commands.command()
    async def попит(self, ctx,*, description: str = None):
        await ctx.message.delete()
        emb = discord.Embed(
            title="<a:pro:871662029025443892> ПОПИТ",
            description="||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||"
	                "||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||"
	                "||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||"
	                "||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||"
	                "||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||"
	                "||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||"
	                "||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||"
	                "||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||"
	                "||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||"
	                "||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||"
	                "||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||"
	                "||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||"
	                "||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||"
	                "||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||"
	                "||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||"
	                "||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||||⚪️||"
	                "||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||"
	                "||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||"
	                "||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||"
	                "||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||||🔵||"
	                "||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||"
	                "||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||"
	                "||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||"
	                "||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||||🔴||"
        )
        emb.set_author(name=ctx.author.name, icon_url = ctx.author.avatar_url)
        await ctx.send(embed=emb)
	
    @commands.command()
    async def woof(self, ctx):
        embed = discord.Embed(color=0x00FFFF)
        embed.set_image(url=nekos.img('woof'))
        await ctx.send(embed = embed)

    @commands.command()
    async def cat(self, ctx):
        r = random.choice([imgs])
        embed = discord.Embed(title='cat', description=f'{r}', color=base_color)
        await ctx.send(embed = embed)

    @commands.command()
    async def ava(self, ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author
        embed = discord.Embed(
            title=f"Аватар {member}", 
            color=base_color
            )
        embed.set_image(url=member.avatar_url)
        await ctx.send(embed=embed)


def setup(client):
	client.add_cog(FUNK(client))