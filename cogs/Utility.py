import base64
import random
import binascii
import asyncio
import aiohttp
import json
import discord
import os
#import requests
import pytz
import datetime
import youtube_dl
from discord import Game
from discord.ext import commands
from discord.ext.commands import Bot

BOT_PREFIX = ("~", "&")
client = Bot(command_prefix=BOT_PREFIX)

class Utility(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, ctx):
        if ctx.guild.name == "The Tavern":
            for channel in ctx.guild.channels:
                if str(channel) == "the-bar":
                    await client.get_channel(612524089730531348).send(f"""Hello and Welcome {ctx.mention}! To The Tavern!""")

    @commands.command(brief="Only for use in the tavern")
    async def sethex(self, ctx, val: str):
        value = discord.Colour(value=int(val, 16))
        embeded = discord.Embed(
            title='Colour Changed',
            colour=value
        )
        embeded.set_thumbnail(url="https://www.colorhexa.com/" + val + ".png")
        embeded.add_field(name='Role Colour Changed', value='Successfully changed' + ctx.message.author.display_name + '\'s role colour to **' + str(value) + "**")
        for role in ctx.guild.roles:
            if role.name == "Ivy" and ctx.message.author.id == 202428607610486786:
                await role.edit(colour=value)
                await ctx.send(embed=embeded)
            elif role.name == "timtams" and ctx.message.author.id == 344984109833256961:
                await role.edit(colour=value)
                await ctx.send(embed=embeded)
            elif role.name == "Chickaen" and ctx.message.author.id == 517853706817896460:
                await role.edit(colour=value)
                await ctx.send(embed=embeded)
            elif role.name == "Red" and ctx.message.author.id == 505109455982034944:
                await role.edit(colour=value)
                await ctx.send(embed=embeded)
            elif role.name == "Mental" and ctx.message.author.id == 424959492606656522:
                await role.edit(colour=value)
                await ctx.send(embed=embeded)
            elif role.name == "Jay" and ctx.message.author.id == 518198365272539147:
                await role.edit(colour=value)
                await ctx.send(embed=embeded)
            elif role.name == "Carl" and ctx.message.author.id == 393827547873280000:
                await role.edit(colour=value)
                await ctx.send(embed=embeded)
            elif role.name == "idoncare" and ctx.message.author.id == 117046427837792256:
                await role.edit(colour=value)
                await ctx.send(embed=embeded)
            elif role.name == "Brush" and ctx.message.author.id == 585171748060659752:
                await role.edit(colour=value)
                await ctx.send(embed=embeded)

    @commands.command()
    async def time(self, ctx, name=""):
        check = 1
        if name == "lime" or name == "carl" or name == "mental" or name == "wale" or name == "wubba" or name == "rubik":
            tz = pytz.timezone('US/Eastern')
        elif name == "satan" or name == "red" or name == "jay" or name == "idc" or name == "brush":
            tz = pytz.timezone('US/Central')
        elif name == "ivy" or name == "tt":
            tz = pytz.timezone('Australia/NSW')
        elif name == "tomer":
            tz = pytz.timezone('Israel')
        elif name == "memes" or name == "twg":
            tz = pytz.timezone('PST8PDT')
        elif name == "sma":
            tz = pytz.timezone('Asia/Singapore')
        elif name == "mlg":
            tz = pytz.timezone('WET')
        elif name == "rigin":
            tz = pytz.timezone('America/Fortaleza')
        elif name =="green":
            tz = pytz.timezone('Europe/Amsterdam')
        else:
            await ctx.send("Invalid Name")
            check = 0
        if check == 1:
            today = datetime.datetime.now(tz)
            await ctx.send(today.strftime("%d-%m-%Y | %I:%M:%S %p"))

    @commands.command()
    async def randcolour(self, ctx):
        hexval = [ '0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F',]
        msg = ''.join(random.choices(hexval, k=6))
        await ctx.send('#' + msg)

    @commands.command()
    async def addrole(self, ctx, rolename=""):
        user = ctx.message.author
        check = 1
        role = ""
        embeded = discord.Embed(
            title='Adding Role',
            colour=discord.Colour.default()
        )
        embeded.set_thumbnail(url=user.avatar_url)
        if rolename == "birb":
            role = "Birb"
        elif rolename == "mudae":
            role = "MudaeBot"
        elif rolename == "pokecord":
            role = "Pok3cord"
        elif rolename == "nsfw":
            role = "Bathroom Key (NSFW)"
        else:
            await ctx.send("Invalid Role")
            check = 0
        if check == 1:
            role1 = discord.utils.get(ctx.guild.roles, name=role)
            if role1 in user.roles:
                embeded.add_field(name=role, value="Failed to add role to " + user.display_name + " as they already have it.", inline=False)
                await ctx.send(embed=embeded)
            else:
                embeded.add_field(name=role, value="Successfully added role to " + user.display_name, inline=False)
                await ctx.send(embed=embeded)
                await user.add_roles(role1)

    @commands.command()
    async def removerole(self, ctx, rolename=""):
        user = ctx.message.author
        check = 1
        role = ""
        embeded = discord.Embed(
            title='Removing Role',
            colour=discord.Colour.default()
        )
        embeded.set_thumbnail(url=user.avatar_url)
        if rolename == "birb":
            role = "Birb"
        elif rolename == "mudae":
            role = "MudaeBot"
        elif rolename == "pokecord":
            role = "Pok3cord"
        elif rolename == "nsfw":
            role = "Bathroom Key (NSFW)"
        else:
            await ctx.send("Invalid Role")
            check = 0
        if check == 1:
            role1 = discord.utils.get(ctx.guild.roles, name=role)
            if role1 not in user.roles:
                embeded.add_field(name=role, value="Failed to remove role to " + user.display_name + " as they do not have it.", inline=False)
                await ctx.send(embed=embeded)
            else:
                embeded.add_field(name=role, value="Successfully removed role from " + user.display_name, inline=False)
                await ctx.send(embed=embeded)
                await user.remove_roles(role1)

def setup(client):
    client.add_cog(Utility(client))