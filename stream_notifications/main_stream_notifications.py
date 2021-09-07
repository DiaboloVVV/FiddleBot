import discord
from discord.ext import commands
from discord.utils import get
import asyncio


class streamnotifs(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.color = 0x1D474C

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        member = await self.client.fetch_user(204024542559993856)
        # guild = client.guilds[1]
        emotes = ['✅', '❓', '❌']
        chan_id = 835952751682388019
        mess_id = 835962082514960384
        main_lobby = 362024296031322133
        time = (15)
        toMention = "<@&835956566293086238>"
        x = 0
        if payload.channel_id == chan_id:
            if payload.emoji.name == emotes[0]:
                channel = self.client.get_channel(chan_id)
                message = await channel.fetch_message(mess_id)
                reaction = get(message.reactions, emoji=payload.emoji.name)
                if reaction and reaction.count > 1:
                    message_chan = self.client.get_channel(main_lobby)
                    await message.remove_reaction(emotes[0], member)
                    mess = await message.channel.send(
                        f'You picked option nr. 1, sending notification in 15s on {message_chan.mention} channel'
                    )
                    await asyncio.sleep(time)
                    await mess.delete()
                    x = 1
            elif payload.emoji.name == emotes[1]:
                channel = self.client.get_channel(chan_id)
                message = await channel.fetch_message(mess_id)
                reaction = get(message.reactions, emoji=payload.emoji.name)
                if reaction and reaction.count > 1:
                    message_chan = self.client.get_channel(main_lobby)
                    await message.remove_reaction(emotes[1], member)
                    mess = await message.channel.send(
                        f'You picked option nr. 2, sending notification in 15s on {message_chan.mention} channel'
                    )
                    await asyncio.sleep(time)
                    await mess.delete()
                    x = 2
            elif payload.emoji.name == emotes[2]:
                channel = self.client.get_channel(chan_id)
                message = await channel.fetch_message(mess_id)
                reaction = get(message.reactions, emoji=payload.emoji.name)
                if reaction and reaction.count > 1:
                    message_chan = self.client.get_channel(main_lobby)
                    await message.remove_reaction(emotes[2], member)
                    mess = await message.channel.send(
                        f'You picked option nr. 3, sending notification in 15s on {message_chan.mention} channel'
                    )
                    await asyncio.sleep(time)
                    await mess.delete()
                    x = 3
            if x == 1:
                channel = self.client.get_channel(main_lobby)
                file = discord.File("./imgs/twitch_logo.png",
                                    filename="twitch_logo.png")
                await channel.send(f'{toMention}')
                twitch_mess = discord.Embed(
                    title='Stix is streaming!\n',
                    description='https://www.twitch.tv/kingstix \n'
                                'https://www.twitch.tv/kingstix \n'
                                'https://www.twitch.tv/kingstix \n',
                    color=0x6441a5)
                twitch_mess.set_thumbnail(url='attachment://twitch_logo.png')
                twitch_mess.set_footer(
                    text=f'If you want to be tagged go to #roles tab.')
                await channel.send(file=file, embed=twitch_mess)
            elif x == 2:
                channel = self.client.get_channel(main_lobby)
                file = discord.File("./imgs/twitch_logo.png",
                                    filename="twitch_logo.png")
                await channel.send(f'{toMention}')
                twitch_mess2 = discord.Embed(
                    title='Stix live will be delayed!\n',
                    description='https://www.twitch.tv/kingstix \n'
                                'https://www.twitch.tv/kingstix \n'
                                'https://www.twitch.tv/kingstix \n',
                    color=0x6441a5)
                twitch_mess2.set_thumbnail(url='attachment://twitch_logo.png')
                twitch_mess2.set_footer(
                    text=f'If you want to be tagged go to #roles tab.')
                await channel.send(file=file, embed=twitch_mess2)
            elif x == 3:
                channel = self.client.get_channel(main_lobby)
                file = discord.File("./imgs/twitch_logo.png",
                                    filename="twitch_logo.png")
                await channel.send(f'{toMention}')
                twitch_mess3 = discord.Embed(
                    title='Stix will not be live today! \n',
                    description='https://www.twitch.tv/kingstix \n'
                                'https://www.twitch.tv/kingstix \n'
                                'https://www.twitch.tv/kingstix \n',
                    color=0x6441a5)
                twitch_mess3.set_thumbnail(url='attachment://twitch_logo.png')
                twitch_mess3.set_footer(
                    text=f'If you want to be tagged go to #roles tab.')
                await channel.send(file=file, embed=twitch_mess3)

def setup(client):
    client.add_cog(streamnotifs(client))
