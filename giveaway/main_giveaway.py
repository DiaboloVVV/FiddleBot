import discord
from discord.ext import commands
from discord.utils import get
import datetime
from datetime import date, timedelta
import time
import sched
import calendar
from dateutil import tz
import asyncio
import random
import sqlite3
import os
import os.path


class giveaway(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.color = 0x1D474C
        dbcreate()

    async def embedUpdate(self):
        counting = 0
        message_id, message_channel_id, prize, time, sampleDate, finished = dbembedupdate()
        while time > 0:
            await asyncio.sleep(600)
            time -= 600
            counting += 1
            conn = sqlite3.connect('giveaway/giveaway.db')
            c = conn.cursor()
            c.execute("UPDATE giveaway_table SET timeseconds=? WHERE id=(SELECT max(id) FROM giveaway_table)", (time,))
            c.execute("SELECT * FROM giveaway_table WHERE id=(SELECT max(id) FROM giveaway_table)")
            print(c.fetchall())
            conn.commit()
            conn.close()
            if counting == 3:
                counting = 0
                newEmbed = discord.Embed(
                    title=f"<:ebe:849286902174711881> TRY YOUR LUCK TO WIN: {prize}! <:ebecat:849286936375066624>",
                    description=f"\n| To participate in giveaway **REACT** with 🎉\n\n| Time remaining:  **{timeRemaning(time)}**",
                    color=self.color)
                newEmbed.set_footer(text=f" Giveaway will end at: {sampleDate} CST")

                message = await self.client.get_channel(message_channel_id).fetch_message(message_id)
                await message.edit(embed=newEmbed)

        channel = self.client.get_channel(message_channel_id)
        new_msg = await channel.fetch_message(message_id)
        users = await new_msg.reactions[0].users().flatten()
        users.pop(users.index(self.client.user))

        winner = random.choice(users)
        member = await new_msg.guild.fetch_member(winner.id)
        # role = get(member.guild.roles, name="giveaway-winner")
        # await member.add_roles(role)

        await channel.send(
            f"Congratulations {winner.mention} you have won!.\nYou have 24h to contact Administrators on # to get ur {prize}")
        conn = sqlite3.connect('giveaway/giveaway.db')
        c = conn.cursor()
        c.execute("UPDATE giveaway_table SET finished=1 WHERE id=(SELECT max(id) FROM giveaway_table)")
        conn.commit()
        conn.close()

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def remove(self, ctx):
        dbdel()

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def greset(self, ctx):
        givreset()

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def fixupdate(self, ctx):
        await ctx.channel.send('fix')
        await self.embedUpdate()
        print('fixed')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def gstart(self, ctx):
        await ctx.send("Answer within 15seconds.\n")
        q = ["Where do you want to host giveway? (ping the channel)",
             "How long does the giveaway should last?",
             "What is the prize?"]

        ans = []

        def validation(currentMessage):
            return currentMessage.author == ctx.author and currentMessage.channel == ctx.channel

        for i in q:
            await ctx.send(i)

            try:
                msg = await self.client.wait_for('message', timeout=15.0, check=validation)
            except asyncio.TimeoutError:
                await ctx.send('You didn\'t enter message in time')
                return
            else:
                ans.append(msg.content)
        try:
            channel_id = int(ans[0][2:-1])
        except:
            await ctx.send("You didn't ping channel properly.")
            return

        channel = self.client.get_channel(channel_id)
        time = convert(ans[1])
        if time == -1:
            await ctx.send("You didn't answer the time correctly. Use s|m|h|d")
            return
        elif time == -2:
            await ctx.send("Time must be an integer.")
            return
        global prize
        prize = ans[2]
        await ctx.send(f"The giveaway will be in {channel.mention} and will last {ans[1]}")

        # embed = discord.Embed(
        #     title="Giveaway!",
        #     description=f"{prize}",
        #     color= 0x006400
        # )
        # embed.add_field(
        #     name="Hosted by:",
        #     value=ctx.author.mention
        # )
        # embed.set_footer(
        #     text=f"Ends {ans[1]} from now!"
        # )
        end2 = datetime.datetime.utcnow()
        end = end2 - datetime.timedelta(seconds=(3600 * 5)) + datetime.timedelta(seconds=time) - datetime.timedelta(microseconds=end2.microsecond)
        embed = discord.Embed(
            title=f"<:ebe:849286902174711881> TRY YOUR LUCK TO WIN: {prize}! <:ebecat:849286936375066624>",
            description=f"\n| To participate in giveaway **REACT** with 🎉\n\n| Time remaining:  **{timeRemaning(time)}**",
            color=self.color,
        )
        # file2 = discord.File("./imgs/confetti.gif", filename="confetti.gif")
        # embed.set_author(name=f'<:ebe:849286902174711881> You have a chance to win: {prize}! <:ebecat:849286936375066624>', icon_url='')  # can't bold text
        # embed.set_thumbnail(url='attachment://confetti.gif')
        # embed.set_footer(text=f"Giveaway started at {time}\n CST") # , value=f"{end} from now!")      giveaway kończy sie za X czasu
        embed.set_footer(text=f" Giveaway will end at: {end} CST")
        # file = discord.File("./imgs/Giveaway.png", filename="Giveaway.png")
        # e = discord.Embed(title='',description='',color=self.color)
        # e.set_image(url='attachment://Giveaway.png')
        # await channel.send(file=file, embed=e)
        my_msg = await channel.send(embed=embed)

        await my_msg.add_reaction("🎉")

        dbdata(my_msg.id, channel_id, prize, time, end)  # adding data to database
        await self.embedUpdate()

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def reroll(self, ctx):
        channel = ctx.message.channel
        giveaway_message_id, prize = dbinfo()
        try:
            new_msg = await channel.fetch_message(giveaway_message_id)
        except:
            await ctx.send("The id was entered incorrectly")
            return
        users = await new_msg.reactions[0].users().flatten()
        users.pop(users.index(self.client.user))
        winner = random.choice(users)
        member = await new_msg.guild.fetch_member(winner.id)
        # role = get(member.guild.roles, name="giveaway-winner")
        # await member.add_roles(role)
        await channel.send(f"Congratulations! New winner of {prize} is {winner.mention}")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def roll(self, ctx):
        channel = ctx.message.channel
        giveaway_message_id, prize = dbinfo()
        try:
            new_msg = await channel.fetch_message(giveaway_message_id)
        except:
            await ctx.send("The id was entered incorrectly")
            return
        users = await new_msg.reactions[0].users().flatten()
        users.pop(users.index(self.client.user))
        winner = random.choice(users)
        member = await new_msg.guild.fetch_member(winner.id)
        # role = get(member.guild.roles, name="giveaway-winner")
        # await member.add_roles(role)
        await channel.send(
            f"Congratulations {winner.mention} you have won!.\nYou have 24h to contact Administrators on # to get ur {prize}")


def tableExists():  # checking if table exists
    conn = sqlite3.connect('giveaway/giveaway.db')
    c = conn.cursor()
    check = c.execute(
        """SELECT count(*) FROM sqlite_master WHERE type='table' AND name='giveaway_table';"""
    )
    conn.commit()
    conn.close()
    return check


def creatingDB():
    if os.path.isfile('giveaway/giveaway.db'):
        print('Database already exists!')
        return True
    else:
        conn = sqlite3.connect('giveaway/giveaway.db')
        c = conn.cursor()
        c.execute("""
                    CREATE TABLE giveaway_table (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    message_id INTEGER,
                    message_channel_id INTEGER,
                    prize TEXT,
                    timeseconds INTEGER,
                    sampleDate timestamp,
                    finished BOOL);""")
        conn.commit()
        conn.close()
        print("Database and table has been created")
        return False


def dbcreate():
    creatingDB()
    conn = sqlite3.connect('giveaway/giveaway.db')
    c = conn.cursor()
    if not tableExists():
        c.execute("""
                    CREATE TABLE giveaway_table (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    message_id INTEGER,
                    message_channel_id INTEGER,
                    prize TEXT,
                    timeseconds INTEGER,
                    sampleDate timestamp,
                    finished BOOL);""")
        print('Creating table')
        conn.commit()
    else:
        print('Table already exists, passing...')
        pass
    conn.commit()
    conn.close()


def dbdata(message_id, message_channel_id, prize, seconds, time):
    conn = sqlite3.connect('giveaway/giveaway.db')
    c = conn.cursor()
    c.execute(
        "INSERT INTO 'giveaway_table' ('id', 'message_id', 'message_channel_id', 'prize','timeseconds', 'sampleDate', 'finished') VALUES (NULL, ?,?,?,?,?,?)",
        (
            message_id,
            message_channel_id,
            prize,
            seconds,
            time,
            0,
        ))
    c.execute("SELECT * FROM giveaway_table")
    print(c.fetchall())
    conn.commit()
    conn.close()


def dbembedupdate():
    conn = sqlite3.connect('giveaway/giveaway.db')
    c = conn.cursor()
    c.execute(
        "SELECT message_id,message_channel_id,prize,timeseconds, sampleDate, finished FROM giveaway_table WHERE id=(SELECT max(id) FROM giveaway_table)"
    )
    message_id, message_channel_id, prize, timeseconds, sampleDate, finished = c.fetchone(
    )
    conn.commit()
    conn.close()
    return message_id, message_channel_id, prize, timeseconds, sampleDate, finished


def dbinfo():
    conn = sqlite3.connect('giveaway/giveaway.db')
    c = conn.cursor()
    c.execute(
        "SELECT message_id,prize FROM giveaway_table WHERE id=(SELECT max(id) FROM giveaway_table)"
    )
    id, prize = c.fetchone()
    conn.commit()
    conn.close()
    return id, prize


def givreset():
    conn = sqlite3.connect('giveaway/giveaway.db')
    c = conn.cursor()
    c.execute("DELETE FROM giveaway_table")
    conn.commit()
    conn.close()


# insert correct timeseconds
def fixupdate():
    conn = sqlite3.connect('giveaway/giveaway.db')
    c = conn.cursor()
    c.execute(
        "UPDATE giveaway_table SET timeseconds=7800 WHERE id=(SELECT max(id) FROM giveaway_table)"
    )
    conn.commit()
    c.execute("SELECT * FROM giveaway_table")
    print(c.fetchall())
    conn.commit()
    conn.close()
    print('updated db')


#  153000
# def givcheck():
#     conn = sqlite3.connect('giveaway/giveaway.db')
#     c = conn.cursor()
#     c.execute("SELECT finished FROM giveaway_table WHERE id=(SELECT max(id) FROM giveaway_table)")
#     finished = c.fetchone()
#     conn.commit()
#     conn.close()
#     if finished[0] == 0:
#         print("Not finished")
#         client = commands.Bot(command_prefix="!")
#         cla = administrator(client)
#         await cla.embedUpdate()
#     else:
#         pass


def dbdel():
    if os.path.exists("giveaway/giveaway.db"):
        os.remove("giveaway/giveaway.db")
        print("Database has been removed")
    else:
        print("The file doesn't exist")


def convert(time):
    pos = ["s", "m", "h", "d"]

    time_dict = {"s": 1, "m": 60, "h": 3600, "d": 3600 * 24}

    unit = time[-1]

    if unit not in pos:
        return -1
    try:
        val = int(time[:-1])
    except:
        return -2

    return val * time_dict[unit]


def timeRemaning(seconds):
    a = str(seconds // 3600)
    # print('more than 48h but works')
    b = str((seconds % 3600) // 60)
    if int(a) > 48:
        c = str((seconds // 3600) // 24)
        d = "{} days {} hours".format(c, b)
        return d
    else:
        d = "{} hours {} mins".format(a, b)
        return d

def setup(client):
    client.add_cog(giveaway(client))