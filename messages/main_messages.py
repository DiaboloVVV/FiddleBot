import discord
from discord.ext import commands
from discord.utils import get

class messages(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.color = 0x1D474C

    @commands.command()
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def ldumb(self, ctx):
        if ctx.message.author == self.client.user:
            return
        if ctx.message.content == '$ldumb':
            await ctx.channel.send('L DUMBLEDORE LOOL')


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def rules(self, ctx):
        channel = self.client.get_channel(836002072058265621)
        file = discord.File("./imgs/rulesleft.png", filename="rulesleft.png")
        e = discord.Embed(title='', description='', color=self.color)
        e.set_image(url='attachment://rulesleft.png')
        await channel.send(file=file, embed=e)
        e = discord.Embed(title='', description='', color=self.color)
        e.add_field(name='**1.) Discord ToS.**', value="This goes without saying, if you've been seen breaking discord"
                                                       "ToS you will be punished depending on the severity of the situation.",
                    inline=False)
        e.add_field(name='**2.) No NSFW content.**',
                    value='NSFW content will not be tolerated no matter the situation ', inline=False)
        e.add_field(name='**3.) Respect KingStix and Staff.**',
                    value='Any disrespect and toxicity towards KingStix and his Staff members'
                          'will result in punishment', inline=False)
        e.add_field(name='**4.) Respect other members of the server.**',
                    value=' Be nice to others/No harassment/Bullying.', inline=False)
        e.add_field(name='**5.) No Spamming.**',
                    value='This goes without saying, any spamming, flooding chat with CAPS '
                          'will be punished.', inline=False)
        e.add_field(name='**6.) No advertising**',
                    value='Advertising without permission from Moderators will result in punishment.', inline=False)
        e.add_field(name='**7.) Use your common sense.**',
                    value='Use your common sense "oh, but that wasn\'t specifically stated in the rules!'
                          ' Yeah, well it was probably stupid and you\'re going to get punished for it. Use your common sense before doing something.'
                          ' If you\'re not sure, and want to avoid getting in trouble, ask a Moderator.', inline=False)
        await channel.send(embed=e)
        e = discord.Embed(title='', description='', color=self.color)
        e.add_field(name='**React with <:KingStix:495646970384351242>  to Access The Server**',
                    value="By accessing to the server you are automatically accepting the rules and becoming a member.")
        await channel.send(embed=e)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def roles(self, ctx):
        file = discord.File("./imgs/rolesleft.png", filename="rolesleft.png")
        e = discord.Embed(title='', description='', color=self.color)
        e.set_image(url='attachment://rolesleft.png')
        # e.set_image(url='https://im6.ezgif.com/tmp/ezgif-6-05670fead996.gif')   # here will be roles banner not rulesX2
        await ctx.channel.send(file=file, embed=e)
        levels = {
            'le50': 835204904200699957,
            'le40': 833879990801399889,
            'le30': 833879701855404059,
            'le20': 833879416811552778,
            'le10': 833879292760686602,
            'le5': 833879048539209768
        }
        le50 = get(ctx.guild.roles, id=levels["le50"])
        le40 = get(ctx.guild.roles, id=levels["le40"])
        le30 = get(ctx.guild.roles, id=levels["le30"])
        le20 = get(ctx.guild.roles, id=levels["le20"])
        le10 = get(ctx.guild.roles, id=levels["le10"])
        le5 = get(ctx.guild.roles, id=levels["le5"])

        e = discord.Embed(
            title='**<:GASM:774420336049389609> You can get diffrent color by being active on the server. <:EVEWAVE:774420313454805012>**',
            description=
            'Every minute that you\'re messaging, you randomly gain between 15 and 25 XP.'
            '__To avoid spamming__, earning XP is limited to __once a minute per user__.'
            f'In the server, you type !rank in {self.client.get_channel(438749366623141889).mention} to see your rank and level.\n'
            f'~ Level 5  ~  {le5.mention} \n'
            f'~ Level 10 ~ {le10.mention} \n'
            f'~ Level 20 ~ {le20.mention} \n'
            f'~ Level 30 ~ {le30.mention} \n'
            f'~ Level 40 ~ {le40.mention} \n'
            f'~ Level 50 ~ {le50.mention}\n'
            f'When you are **RANK 1** on the server leaderboard, you\'ll get {get(ctx.guild.roles, id=458991750590103571).mention} with color of yours.',
            color=self.color)
        await ctx.channel.send(embed=e)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def roles2(self, ctx):
        e = discord.Embed(
            title='**<:GASM:774420336049389609> Assign Region&Position roles <:EVEYUMMI:774420328763490335>**',
            description='We mostly talk about **League Of Legends**.'
                        ' So in order to find someone to play with, you can **choose region** you are playing and **position** you are maining.',
            color=self.color)
        await ctx.channel.send(embed=e)
        e = discord.Embed(title='Choose your position!',
                          description=f'<:TOP:835223543839064131> *Top lane* »» {get(ctx.guild.roles, id=835239647650775131).mention} \n'
                                      f'<:MIDDLE:835223544148787240> *Mid lane* »» {get(ctx.guild.roles, id=835239919823618048).mention} \n'
                                      f'<:JUNGLE:835223544131485706> *Jungle* »»  {get(ctx.guild.roles, id=835240061725048872).mention}   \n'
                                      f'<:ADC:835223544148787200> *Bot lane* »» {get(ctx.guild.roles, id=835240181489336343).mention} \n'
                                      f'<:SUPPORT:835223543855054930> *Support* »» {get(ctx.guild.roles, id=835240288967983174).mention}  \n',
                          color=self.color)
        msg_1 = await ctx.channel.send(embed=e)
        await msg_1.add_reaction('<:TOP:835223543839064131>')
        await msg_1.add_reaction('<:MIDDLE:835223544148787240>')
        await msg_1.add_reaction('<:JUNGLE:835223544131485706>')
        await msg_1.add_reaction('<:ADC:835223544148787200>')
        await msg_1.add_reaction('<:SUPPORT:835223543855054930>')

        region_roles = {
            'oce': 801573190551863326,
            'na': 801573295820374016,
            'kr': 801573424098181130,
            'jp': 801573572413882488,
            'euw': 801573600011485194,
            'eune': 801573768874950677,
            'br': 801573996335464458,
            'las': 801574146219180113,
            'lan': 801574191786491984,
            'ru': 801574249587671101,
            'tr': 801574292298661938,
            'gr': 801574443050336288
        }
        e = discord.Embed(title='Choose your region!',
                          description=f"<:na:835282302908760094> North America »»{get(ctx.guild.roles, id=region_roles['na']).mention} \n"
                                      f"<:euw:835282302703632475> Europe West »» {get(ctx.guild.roles, id=region_roles['euw']).mention} \n"
                                      f"<:eune:835282302396792893> Europe Nordic & East »»  {get(ctx.guild.roles, id=region_roles['eune']).mention} \n"
                                      f"<:tr:835282302543069205> Turkey »» {get(ctx.guild.roles, id=region_roles['tr']).mention} \n"
                                      f"<:jp:835282302484611133> Japan »» {get(ctx.guild.roles, id=region_roles['jp']).mention} \n"
                                      f"<:kr:835282302560370813> Republic of Korea »» {get(ctx.guild.roles, id=region_roles['kr']).mention} \n"
                                      f"<:oce:835282302899716146> Oceania »» {get(ctx.guild.roles, id=region_roles['oce']).mention} \n"
                                      f"<:br:835282302447124491> Brazil »» {get(ctx.guild.roles, id=region_roles['br']).mention} \n"
                                      f"<:gr:835282302841782312> Garena »» {get(ctx.guild.roles, id=region_roles['gr']).mention} \n"
                                      f"<:las:835282303118475264> Latin America South »» {get(ctx.guild.roles, id=region_roles['las']).mention} \n"
                                      f"<:lan:835282302795644968> Latin America North »» {get(ctx.guild.roles, id=region_roles['lan']).mention} \n"
                                      f"<:ru:835282302967087124> Russia »» {get(ctx.guild.roles, id=region_roles['ru']).mention} \n",
                          color=self.color)

        msg_1 = await ctx.channel.send(embed=e)

        # e = discord.Embed(title="Giveaway&Twitch Notification", description="")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def notifi(self, ctx):
        rank_twitch = 835956566293086238
        rank_give = 835182357802909747
        nnoti_mess = discord.Embed(title='<:GASM:774420336049389609> Notification roles <:EVEWAVE:774420313454805012>',
                                   description='If you want to stay up to date with every **__Stream__** or **__Giveaway__**, **react** to the corresponding role.\n\n'
                                               f'<:money:836311389777559592> »» *Giveaway Notifications* »» {get(ctx.guild.roles, id=rank_give).mention}\n\n'
                                               f'<:twitch:836311971770531840> »» *Stream Notifications* »» {get(ctx.guild.roles, id=rank_twitch).mention}',
                                   color=0x1D474C)
        msg = await ctx.channel.send(embed=nnoti_mess)
        await msg.add_reaction('<:money:836311389777559592>')
        await msg.add_reaction('<:twitch:836311971770531840>')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def banner(self, ctx):
        e = discord.Embed(title="Stream SURVEY", description="1) Steam will take place as planned. »» ✅\n"
                                                             "2) Steam will be delayed. »» ❓\n"
                                                             "3) Steam will not take place. »» ❌",
                          color=self.color)
        msg = await ctx.send(embed=e)

        await msg.add_reaction('✅')
        await msg.add_reaction('❓')
        await msg.add_reaction('❌')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def lfg(self, ctx):
        rank_give = 841048319312265237
        noti_mess = discord.Embed(title='🔎 ENABLE Looking For Game channel! 🔍',
                                  description='If you __want the access__ to the LFG channel **react** below.\n'
                                              'After reacting, the LFG channel will **APPEAR**. If you **UN-REACT**, the LFG channel will **DISAPPEAR**.\n\n'
                                              f'🔊 »» *Enable Looking For Game Channel* »» {get(ctx.guild.roles, id=rank_give).mention}\n\n',
                                  color=self.color)
        await ctx.channel.send(embed=noti_mess)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def color(self, ctx):
        e = discord.Embed(
            title="<:EVEWAVE:774420313454805012> Your reward for helping the server! <:GASM:774420336049389609>",
            description='For being helpful to Moderation and by setting a good example to others users you can'
                        ' __choose__ your __nickname color__.\n'
                        '**React** to the color you would like to have,'
                        ' if you want to **change** the color'
                        ' **unreact** last color and __react to the new one__.', color=0x1D474C)

        await ctx.channel.send(embed=e)
        s1 = "<@&847855121269653514>"
        s2 = "<@&847854802906120192>"
        f1 = "<@&847854623494111302>"
        f2 = "<@&847854401040941087>"
        t1 = "<@&847854222577369140>"
        t2 = "<@&847854050666217472>"
        m1 = "<@&847853821773217795>"
        m2 = "<@&847853543347060737>"
        ma1 = "<@&847853008871620608>"
        ma2 = "<@&847852283185987585>"

        e = discord.Embed(
            title="<:heart_eve:840590130623938560> A color pack for LIGHT side fans! <:heart_eve:840590130623938560>",
            description=f"<:s1:847909771360862260> »» {s1}\n "
                        f"<:f1:847910291798491177> »» {f1}\n "
                        f"<:t1:847909771562713089> »» {t1}\n "
                        f"<:m1:847909771633754182> »» {m1}\n "
                        f"<:ma1:847909771465588806> »» {ma1}\n",
            color=0x1D474C)
        await ctx.channel.send(embed=e)
        e = discord.Embed(
            title="<:heart_eve:840590130623938560> A color pack for DARK side fans! <:heart_eve:840590130623938560>",
            description=f"<:s2:847909771550261298> »» {s2}\n "
                        f"<:f2:847909771340021762> »» {f2}\n "
                        f"<:t2:847909771637948437> »» {t2}\n "
                        f"<:m2:847909771687493642> »» {m2}\n "
                        f"<:ma2:847909771524440115> »» {ma2}\n",
            color=0x1D474C)
        await ctx.channel.send(embed=e)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def faq(self, ctx):
        qua = "<@&335180146216534026>"
        twi = "<@&832772299765055488>"
        a0 = "https://cutt.ly/NnoE9nq"
        a1 = "https://cutt.ly/lnoE2Sp"
        a2 = "https://cutt.ly/bnoE0c5"
        a3 = "https://cutt.ly/lnoE1TC"
        a4 = "https://cutt.ly/lnoEM0Y"
        a5 = "https://cutt.ly/enoEN9u"
        a6 = "https://cutt.ly/enoEBFx"
        a7 = "https://cutt.ly/wnoEVuB"
        a8 = "https://cutt.ly/6noELBr"
        yt = "https://www.youtube.com/kingstix"
        twitch = "https://www.twitch.tv/kingstix"
        twitter = "https://twitter.com/kingstixlol?lang=en"
        moba = "https://www.mobafire.com/profile/kingstix-666337"
        coach = "https://docs.google.com/document/d/1S5OfFxyQ4OLFokmiJdQbQFROQmsKFpgpmohILtmfcKA/view"

        e = discord.Embed(
            title='<:EVEWAVE:774420313454805012> Frequently Asked Questions <:EVEYUMMI:774420328763490335>',
            description=" Before asking the Moderation __check the text below__, there's a high chance you'll find an answer to your quesiton.",
            color=0x1D474C)
        e.add_field(name="<:dot:845407967620890696>  Where can I find the Tier List?",
                    value=f"The Tier list is currently only avaible to Twitch Subscribers \n»» {twi}", inline=False)
        e.add_field(name="<:dot:845407967620890696>  I'm subscribed on Twitch but I don't see a Tier List channel.",
                    value="Be sure to **connect** your discord account with Twitch account."
                          "\n***How to connect an account?***   Go to the discord settings, in the **USER SETTINGS** cattegory click on the **Connections** and "
                          "then click on Twitch logo. ", inline=False)
        e.add_field(name="<:dot:845407967620890696>  Does TWITCH PRIME count as a twitch subscription?",
                    value="Yes, a twitch prime subscription "
                          "counts as a normal subscription.", inline=False)

        e.add_field(name="<:dot:845407967620890696>  How long does a warning stay for?",
                    value="A warning stays until your behaviour improves and is noticeable by chatters and mods. **Asking a mod will NOT work**.",
                    inline=False)
        e.add_field(name=f"<:dot:845407967620890696>  What is and how do I get a Squad role?",
                    value=f"{qua} role can be obtained by being active and adding something special to the server, some ***SPICE***.",
                    inline=False)
        e.add_field(name="<:dot:845407967620890696>  How can I know what to post on each channel?",
                    value="If you are not sure what can be posted on channel, check channel description. Each channel has it's own description.",
                    inline=False)
        await ctx.channel.send(embed=e)
        e = discord.Embed(
            title="<:EVEWAVE:774420313454805012> General info about KingStix! <:EVEYUMMI:774420328763490335>",
            description="", color=0x1D474C)
        e.add_field(name="<:dot:845407967620890696>  When does KingStix stream?", value="All week days at 12am CDT.",
                    inline=False)
        e.add_field(name="<:dot:845407967620890696> How to get coached by KingStix?",
                    value=f"Clik [HERE]({coach}) for more infomation about coaching.", inline=False)
        e.add_field(name="<:dot:845407967620890696>  What are KingStix PC specs?",
                    value=f"[Motherboard]({a0}): ASUS Prime Z390-A\n"
                          f"[CPU]({a1}): AMD Ryzen 7 3700X 8-Core 16-Thread\n"
                          f"[GPU]({a2}): Gigabyte GeForce GTX 1070 G1 Gaming\n"
                          f"[RAM]({a3}): Corsair Vengeance LPX 16GB (2x8GB) DDR4 DRAM 3200MHz C16\n "
                          f"[Monitor]({a4}): BenQ ZOWIE XL2411P 24 Inch 144Hz Gaming Monitor\n"
                          f"[Mouse]({a5}): Logitech G502 HERO High Performance Wired Gaming Mouse\n"
                          f"[Keyboard]({a6}): Redragon K552 Red Switches\n"
                          f"[Microphone]({a7}): Audio-Technica AT2020 Cardioid Condenser Studio XLR\n"
                          f"[Headphones]({a8}): Audio-Technica ATH-M50X Professional Studio Monitor Headphones",
                    inline=False)
        e.add_field(name="<:dot:845407967620890696>  Where can I find KingStix?", value=f"[YouTube]({yt}): kingstix \n"
                                                                                        f"[Twitch]({twitch}): kingstix \n"
                                                                                        f"[Twitter]({twitter}): KingStixLoL \n"
                                                                                        f"[MobaFire]({moba}): kingstix")
        e.set_footer(text="Words in blue color are a clickable links.")
        await ctx.channel.send(embed=e)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def plsbot(self, ctx):
        e = discord.Embed(title="How to use Dank Memer and some informations!", description="On this channel you can "
                                                                                            "use a gambling bot - Dank "
                                                                                            "Memer.\nYou can use it by "
                                                                                            "typing **pls <command>**, "
                                                                                            "some commands requires you "
                                                                                            "to ping an user ex. **pls rob "
                                                                                            "@<user>**.\nI hope you'll have "
                                                                                            "fun with bot, it has a lot "
                                                                                            "more functions you can check "
                                                                                            "by clicking on **[THIS](https://dankmemer.lol/commands)**."
                                                                                            "\n *NSFW commands are "
                                                                                            "permamently __disabled__* "
                                                                                            "<:bonk:834118680174395445>"
                                                                                            "\n\n**»» Here you can check the most "
                                                                                            "basic commands. ««**\n\n"
                          , color=0x6441a5)
        e.add_field(name="pls balance", value="Check your actual bank balance.", inline=False)
        e.add_field(name="pls daily", value="Once a day you can claim free money.", inline=False)
        e.add_field(name="pls deposit *<amount>*", value="Transfer money to your bank account.", inline=False)
        e.add_field(name="pls work", value="Gain money by working.", inline=False)
        e.add_field(name="pls blackjack *<amount>* OR pls bj *<amount>*", value="Play a game of blackjack.",
                    inline=False)
        e.add_field(name="pls gamble *<amount>*", value="Play a game of dice.", inline=False)
        e.add_field(name="pls highlow", value="Guess if the number i"
                                              "s higher or lower (quick way to make money).", inline=False)
        e.add_field(name="pls beg", value="Beg for money.", inline=False)
        e.add_field(name="pls steal *@<user>*",
                    value="Try to steal from 20% to 100% of robbed user coins if successful.", inline=False)
        e.add_field(name="pls shop", value="Check what's inside a shop. To buy an item type **pls buy *<item name>***.",
                    inline=False)
        e.add_field(name="pls inventory", value="Shows your equipment, to use an item type **pls use *<item name>***.",
                    inline=False)
        await ctx.channel.send(embed=e)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def twitch(self, ctx):
        rank_twitch = 835142120171110471
        toMention = get(self.guild.roles, id=rank_twitch).mention
        channel = self.client.get_channel(833746339480993812)
        file = discord.File("./imgs/twitch_logo.png", filename="twitch_logo.png")
        await channel.send(f'{toMention}')
        twitch_mess = discord.Embed(title='Stix will be streaming soon!\n',
                                    description='https://www.twitch.tv/kingstix \n'
                                                'https://www.twitch.tv/kingstix \n' 'https://www.twitch.tv/kingstix \n',
                                    color=0x6441a5)
        twitch_mess.set_thumbnail(url='attachment://twitch_logo.png')
        twitch_mess.set_footer(text=f'If you want to be tagged as {toMention} go to #roles tab.')
        await channel.send(file=file, embed=twitch_mess)

        file = discord.File("./imgs/twitch_logo.png", filename="twitch_logo.png")
        await channel.send(f'{toMention}')
        twitch_mess2 = discord.Embed(title='Stix live will be delayed!\n',
                                     description='https://www.twitch.tv/kingstix \n' 'https://www.twitch.tv/kingstix \n' 'https://www.twitch.tv/kingstix \n',
                                     color=0x6441a5)
        twitch_mess2.set_thumbnail(url='attachment://twitch_logo.png')
        twitch_mess2.set_footer(text=f'If you want to be tagged as {toMention} go to #roles tab.')
        await channel.send(file=file, embed=twitch_mess2)

        file = discord.File("./imgs/twitch_logo.png", filename="twitch_logo.png")
        await channel.send(f'{toMention}')
        twitch_mess3 = discord.Embed(title='Stix will not be live today! \n',
                                     description='https://www.twitch.tv/kingstix \n' 'https://www.twitch.tv/kingstix \n' 'https://www.twitch.tv/kingstix \n',
                                     color=0x6441a5)
        twitch_mess3.set_thumbnail(url='attachment://twitch_logo.png')
        twitch_mess3.set_footer(text=f'If you want to be tagged as {toMention} go to #roles tab.')
        await channel.send(file=file, embed=twitch_mess3)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def rangi(self,ctx):
        ranks = {
            'iron': '<:rankIron:886336986288357407>',
            'bronze': '<:rankBronze:886336986099638312>',
            'silver': '<:rankSilver:886336986359660644>',
            'gold': '<:rankGold:886336986284175380>',
            'plat': '<:rankPlatinium:886336986523267122>',
            'diamond': '<:rankDiamond:886336986703613963>',
            'master': '<:rnakMaster:886336986217070663>',
            'grandmaster': '<:rankGrandMaster:886336986200281098>',
            'chall': '<:rankChallenger:886336986166730762>'
        }
        rank_roles = {
            'iron': get(ctx.guild.roles, id=887306807394050058),
            'bronze': get(ctx.guild.roles, id=887307867185631232),
            'silver': get(ctx.guild.roles, id=887308084156985394),
            'gold': get(ctx.guild.roles, id=887308190423859251),
            'plat': get(ctx.guild.roles, id=887308298506879026),
            'diamond': get(ctx.guild.roles, id=887308386297851915),
            'master': get(ctx.guild.roles, id=887308458725113886),
            'grandmaster': get(ctx.guild.roles, id=887308522054905907),
            'chall': get(ctx.guild.roles, id=690744184004542505)
        }
        staff = '<@&845339723575722013>'
        lfg = self.client.get_channel(839943400848752670)
        # <iron rank> Verify your rank! <chall rank> - title \
        e = discord.Embed(title=f'<:ebecat:849286936375066624> Verify your rank! <:ebe:849286902174711881>',
                          description="In order to acquire a role resembling "
                                      "your **League of Legends rank**"
                                      " **__react below__**."
                          # f"Iron »» {iron}\n"
                          # f"Bronze »» {bronze}\n"
                          # f"Silver »» {silver}\n"
                          # f"Gold »» {gold}\n"
                          # f"Platinium »» {plat}\n"
                          # f"Diamond »» {diamond}"
                                      "\nIf your rank is **__Platinium or higher__**"
                                      " please contact someone from an \n **administrator team -> "
                                      f"{staff}** to verify your rank.\n"
                                      "After verification __you'll get a role with your rank.__\n\n"
                                      f"{ranks['iron']} **I**ron »»  {rank_roles['iron'].mention}\n"
                                      f"{ranks['bronze']} **B**ronze »» {rank_roles['bronze'].mention}\n"
                                      f"{ranks['silver']} **S**ilver  »»   {rank_roles['silver'].mention}\n"
                                      f"{ranks['gold']} **G**old »»  {rank_roles['gold'].mention}\n"
                                      f"{ranks['plat']} **P**latinium »»  {rank_roles['plat'].mention}\n"
                                      f"{ranks['diamond']} **D**iamond »»  {rank_roles['diamond'].mention}\n"
                                      f"{ranks['master']} **M**aster »»  {rank_roles['master'].mention}\n"
                                      f"{ranks['grandmaster']} **G**rand**M**aster »»  {rank_roles['grandmaster'].mention}\n"
                                      f"{ranks['chall']} **C**hallenger »»  {rank_roles['chall'].mention}\n"
                                      "\n*Having rank role can help you* "
                                      f"*in finding better duo partner in {lfg.mention}!*"
                          , color=self.color)
        msg = await ctx.channel.send(embed=e)
        for key in ranks:
            if key != 'plat':
                await msg.add_reaction(ranks[key])
            else:
                break


def setup(client):
    client.add_cog(messages(client))