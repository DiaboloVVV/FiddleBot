import discord
from discord.ext import commands
import datetime
from discord.utils import get
import asyncio
import json
import sqlite3
import os



class user_managment(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def prune(self, ctx, amount=1):
        await ctx.channel.purge(limit=amount+1)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def setup(self, ctx):
        guild = ctx.guild
        setupQuestions = [
            "Please ping warn role.",
            "Please ping stage 2 warn role",
            "Where should I log messages? (ping channel)"
        ]
        setupAnswers = []
        for question in setupQuestions:
            await ctx.send(question)

            try:
                answer = await self.client.wait_for('message',timeout=15.0,
                                                    check=lambda message: message.author == ctx.author and message.channel == ctx.channel)
            except asyncio.TimeoutError:
                await ctx.send("You didn\'t answer in time")
                return
            else:
                setupAnswers.append(answer.content)
        setupAsnwersCleared = [y.strip('<>#@&') for y in setupAnswers]
        with open('config.json', 'r+') as jsonFile:
            data = json.load(jsonFile)
            data[str(guild.id)] = {
                "name": f"{guild.name}",
                "warn": f"{str(setupAsnwersCleared[0])}",
                "warn2": f"{str(setupAsnwersCleared[1])}",
                "logChannel": f"{str(setupAsnwersCleared[2])}"
            }
            jsonDataIndent = json.dumps(data, indent=4)
            jsonFile.seek(0)
            jsonFile.write(jsonDataIndent)
            jsonFile.truncate()

    def configFile(self):
        with open('config.json') as jsonFile:
            data = json.load(jsonFile)
        return data

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.User = None, *, reason=None):
        guild = ctx.guild
        if member is None or member == ctx.message.author:
            await ctx.author.send("You cannot ban yourself.")
            return
        if reason is None:
            reason = "Breaking server/discord rules!"
        type = "banned"
        try:
            scrLink = ctx.message.attachments[0].url
            await self.logMessage(ctx, type, member, reason, scrLink)
        except Exception:
            await self.logMessage(ctx, type, member, reason, '')
        await ctx.message.delete()
        await guild.ban(member, reason=reason, delete_message_days=7)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def warn(self, ctx, member: discord.User = None, *, reason=None):
        guild = ctx.guild
        if member is None or member == ctx.message.author:
            await ctx.channel.send("You cannot warn yourself")
            return
        if reason is None:
            reason = "Breaking server/discord rules!"
        try:
            scrLink = ctx.message.attachments[0].url
            reason += "\n" + scrLink
            db_warn(guild, member, reason)
            await self.warnSections(guild, ctx, member, reason, scrLink)
        except:
            db_warn(guild, member, reason)
            await self.warnSections(guild, ctx, member, reason, '')
        await ctx.message.delete()
        await ctx.channel.send(f"Command used succesfully", delete_after=0.5)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def warned(self, ctx):
        guild = ctx.guild
        await ctx.message.delete()
        data = self.configFile()
        channel = self.client.get_channel(int(data[str(guild.id)]["logChannel"]))
        try:
            conn = sqlite3.connect(f'{guild.id}/{guild.id}.db')
            c = conn.cursor()
            row = c.execute(
                """SELECT * FROM warned_users;"""
            ).fetchall()
            conn.commit()
            conn.close()
            e = discord.Embed(
                title="WARNED USERS",
                description="",
                color=0x1D474C
            )
        except sqlite3.OperationalError:
            await channel.send("Database is damaged! To repair just warn someone!")
        for x in range(len(row)):
            if len(e) >= 1024:
                await channel.send(embed=e)
                e = discord.Embed(
                    title="",
                    description="",
                    color=0x1D474C
                )
            e.add_field(name=f'ID: {row[x - 1][1]} \nWHO: {row[x - 1][2]} \nWHEN: {row[x - 1][4]}',
                        value=f'**REASON:** \n{row[x - 1][3]}', inline=False)
        await channel.send(embed=e)


    async def warnSections(self, guild, ctx, member, reason, scrLink):
        data = self.configFile()
        warnRole = get(guild.roles, id=int(data[str(guild.id)]["warn"]))
        warn2Role = get(guild.roles, id=int(data[str(guild.id)]["warn2"]))

        if warn2Role in member.roles:
            type = "banned"
            reason += '\n **BAN FROM WARNINGS.**'
            await self.logMessage(ctx, type, member, reason, scrLink)
            await ctx.guild.ban(member, reason=reason, delete_message_days=7)
        elif warnRole in member.roles:
            type = "warned again"
            await member.add_roles(warn2Role)
            await self.logMessage(ctx, type, member, reason, scrLink)
        else:
            type = "warned"
            await self.logMessage(ctx, type, member, reason, scrLink)
            await member.add_roles(warnRole)



    async def logMessage(self, ctx, type, member, reason, scrLink):
        guild = ctx.guild
        data = self.configFile()
        channel = self.client.get_channel(int(data[str(guild.id)]["logChannel"]))
        if type == None:
            pass
        else:
            try:
                await member.send(f"You have been {type} from {guild.name} for: {reason}")
            except Exception:
                await channel.send("Can\'t send message to the user. User propably doesn\'t accept private messages or he\'s not in the server")
        e = discord.Embed(
            title=f"an user has been {type}".upper(),
            description="",
            color=0xFF0000
        )
        e.add_field(
            name=f"{type} person discord name and tag.".capitalize(),
            value=f"{member}", inline=False
        )
        e.add_field(
            name=f"{type} person's ID:".capitalize(),
            value=f"{member.id}", inline=False
        )
        e.add_field(
            name="Reason:",
            value=f"{reason}"
        )
        e.set_image(url=scrLink)
        e.timestamp = datetime.datetime.utcnow()
        e.set_footer(text='\u200b', icon_url="")
        await channel.send(embed=e)



def db_warn(guild, member, reason):
    if os.path.isdir(f'{guild.id}') and os.path.isfile(f'{guild.id}/{guild.id}.db'):
        try:
            conn = sqlite3.connect(f'{guild.id}/{guild.id}.db')
            c = conn.cursor()
            c.execute("""
                        CREATE TABLE warned_users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        person_id BIGINT,
                        person_tag TEXT,
                        reason TEXT,
                        warndate DATE);""")
            conn.commit()
            conn.close()
            print('Creating warned_users table')
        except Exception:
            # print("Table exists!")
            pass

    elif not os.path.isdir(f'{guild.id}'):
        os.mkdir(f'{guild.id}')
        conn = sqlite3.connect(f'{guild.id}/{guild.id}.db')
        c = conn.cursor()
        c.execute("""
                CREATE TABLE warned_users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                person_id BIGINT,
                person_tag TEXT,
                reason TEXT,
                warndate DATE);""")
        conn.commit()
        conn.close()
    person_id = int(member.id)
    conn = sqlite3.connect(f'{guild.id}/{guild.id}.db')
    c = conn.cursor()
    c.execute(
        "INSERT INTO 'warned_users' ('id', 'person_id', 'person_tag', 'reason', 'warndate') VALUES (NULL,?,?,?,?)",
        (person_id,
         str(member),
         reason,
         datetime.datetime.utcnow(),
         ))
    conn.commit()
    conn.close()


def setup(client):
    client.add_cog(user_managment(client))
