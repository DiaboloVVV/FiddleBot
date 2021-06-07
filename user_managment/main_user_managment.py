import discord
from discord.ext import commands
from discord.utils import get


class user_managment(commands.Cog):
    def __init__(self,client):
        self.client = client
        self.color = 0x1D474C

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def prune(self, ctx, amount=1):
        await ctx.channel.purge(limit=amount+1)


def setup(client):
    client.add_cog(user_managment(client))