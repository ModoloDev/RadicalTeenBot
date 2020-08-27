import discord
import random
import asyncio
import datetime
import yaml
from time import strftime, localtime, time, gmtime, mktime
from discord.utils import get
from discord.ext import commands
from discord.ext.commands import CommandNotFound
from embeds import *
# with open('settings/settings.yaml', 'r') as f: data = yaml.load(f, Loader= yaml.FullLoader)

bot = commands.Bot(command_prefix = ".", help_command= None)
testechannel = bot.get_channel(686763964256092164)
rtchannel = bot.get_channel(678453889263075349)

#Celulas Role
async def RoleCelulas(rtchannel):
    global EkklesiaRole
    EkklesiaRole = get(rtchannel.guild.roles, id=678462920862072852)

    global JudahRole
    JudahRole = get(rtchannel.guild.roles, id=678463157374550017)

    global MaanaimRole
    MaanaimRole = get(rtchannel.guild.roles, id=678463077003427841)

    global AhavaRole
    AhavaRole = get(rtchannel.guild.roles, id=678463327793446913)

    global EliteRole
    EliteRole = get(rtchannel.guild.roles, id=678463392255705109)

    global TeknongramosRole
    TeknongramosRole = get(rtchannel.guild.roles, id=678463256460787732)

    global HovhanessRole
    HovhanessRole = get(rtchannel.guild.roles, id=678467646269685761)

    global MakariasRole
    MakariasRole = get(rtchannel.guild.roles, id=686764850416058378)

async def Celula(EkklesiaRole, JudahRole, MaanaimRole, AhavaRole, EliteRole, TeknongramosRole, HovhanessRole, MakariasRole):

    return [EkklesiaRole.id, JudahRole.id, MaanaimRole.id, AhavaRole.id, EliteRole.id, TeknongramosRole.id, HovhanessRole.id, MakariasRole.id]


#Adms Role
async def AdmsRoles(rtchannel):
    global LideresRole
    LideresRole = get(rtchannel.guild.roles, id=678450377678651392)

    global ADMSRole
    ADMSRole = get(rtchannel.guild.roles, id=679059732119683083)

    global PastoresRole
    PastoresRole = get(rtchannel.guild.roles, id=689875778858385467)

async def Adm(LideresRole, ADMSRole, PastoresRole):

    return [LideresRole.id, ADMSRole.id, PastoresRole.id]

#Role
def Roles(reaction, user):
    if reaction.emoji == "0️⃣":
        Role = EkklesiaRole
    elif reaction.emoji == "1️⃣":
        Role = HovhanessRole
    elif reaction.emoji == "2️⃣":
        Role = TeknongramosRole
    elif reaction.emoji == "3️⃣":
        Role = JudahRole
    elif reaction.emoji == "4️⃣":
        Role = MaanaimRole
    elif reaction.emoji == "5️⃣":
        Role = EliteRole
    elif reaction.emoji == "6️⃣":
        Role = AhavaRole
    '''
    elif reaction.emoji == "7️⃣":
        Role = MakariasRole
    '''

    return Role

async def codcelula(rtchannel):


    global msg_bot
    msg_bot = await rtchannel.send(embed = escolhercelula())

    await msg_bot.add_reaction("0️⃣")
    await msg_bot.add_reaction("1️⃣")
    await msg_bot.add_reaction("2️⃣")
    await msg_bot.add_reaction("3️⃣")
    await msg_bot.add_reaction("4️⃣")
    await msg_bot.add_reaction("5️⃣")
    await msg_bot.add_reaction("6️⃣")
    #await msg_bot.add_reaction("7️⃣")


    #Log
    global logchannel
    global msg_log
    logchannel = bot.get_channel(686371893007089694)
    msg_log = logchannel.send



async def check(ctx, adms):
    return discord.utils.find(lambda x: x.id in adms, ctx.author.roles)



@bot.event
async def on_ready():
    print('ONLINE ' + '(' + strftime("%d/%m/%Y - %H:%M:%S", localtime(mktime(gmtime())-10800)) + ')')
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("Radical Teen ✝"))
    rtchannel = bot.get_channel(678453889263075349)

    await rtchannel.purge(limit = None)

    await RoleCelulas(rtchannel)
    await AdmsRoles(rtchannel)
    await codcelula(rtchannel)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.send(embed = errorcomando())

@bot.event
async def on_member_join(user):
    rtchannel = bot.get_channel(678453889263075349)

    if str(user.bot) == "False":
        await rtchannel.purge(limit = None)

        await user.add_roles(get(rtchannel.guild.roles, id=678463459385540618))

        msg_temp = await rtchannel.send(f'<@!{user.id}>')
        msg_temp2 = await rtchannel.send(embed = bemvindo(user))

        await codcelula(rtchannel)

        await asyncio.sleep(30)
        await msg_temp.delete()
        await msg_temp2.delete()



@bot.event
async def on_message(message):
    rtchannel = bot.get_channel(678453889263075349)
    if message.channel == rtchannel:
        botradical = bot.get_user(686754559531417611)
        botradicalteste = bot.get_user(688243571865682010)
        if message.author.id != botradical.id and message.author.id != botradicalteste.id:
            await message.delete()
        

    message_content = message.content.strip().lower()
    # if "zoom" in message_content:
    #     user = message.author.name
    #     channel = bot.get_channel(message.channel.id)
    #     await message.delete()
    #     msg_temp = await channel.send(embed = zoom(user))
    #     await asyncio.sleep(15)
    #     await msg_temp.delete() 

    if "discord" in message_content:
        channel = bot.get_channel(message.channel.id)
        await asyncio.sleep(15)
        await channel.send(embed = discor1())

      


    await bot.process_commands(message) #ISSO FAZ OS COMANDOS FUNCIONAREM


@bot.event
async def on_reaction_add(reaction, user):
    rtchannel = bot.get_channel(678453889263075349)
    if msg_bot.id == reaction.message.id and user.name != msg_bot.author.name:
        if reaction.emoji == "0️⃣" or reaction.emoji == "1️⃣" or reaction.emoji == "2️⃣" or reaction.emoji == "3️⃣" or reaction.emoji == "4️⃣" or reaction.emoji == "5️⃣" or reaction.emoji == "6️⃣":
            Role = Roles(reaction, user)
            celula = await Celula(EkklesiaRole, JudahRole, MaanaimRole, AhavaRole, EliteRole, TeknongramosRole, HovhanessRole, MakariasRole)

            x = discord.utils.find(lambda x: x.id in celula, user.roles)
            if x == None:
                await user.add_roles(Role)
                await msg_log(embed = logentrou(user.name, Role.name))
                msg_temp = await rtchannel.send(embed = logentrou(user.name, Role.name))
                await asyncio.sleep(5)
                await msg_temp.delete()        
            else:
                x = discord.utils.find(lambda x: x.id == Role.id, user.roles)
                if x != None:
                    msg_temp = await rtchannel.send(embed = mesmacelula(user.name))
                    await asyncio.sleep(5)
                    await msg_temp.delete()
                else:
                    msg_temp = await rtchannel.send(embed = possuicelula(user.name))
                    await asyncio.sleep(5)
                    await msg_temp.delete()
        else:
            await msg_bot.remove_reaction(reaction, user)

    def reactionmsg():
        return reaction, user


@bot.event
async def on_reaction_remove(reaction, user):
    rtchannel = bot.get_channel(678453889263075349)
    if msg_bot.id == reaction.message.id:
        if reaction.emoji == "0️⃣" or reaction.emoji == "1️⃣" or reaction.emoji == "2️⃣" or reaction.emoji == "3️⃣" or reaction.emoji == "4️⃣" or reaction.emoji == "5️⃣" or reaction.emoji == "6️⃣":
            Role = Roles(reaction, user)
            

            x = discord.utils.find(lambda x: x.id == Role.id, user.roles)
            if x != None:
                await user.remove_roles(Role)  
                await msg_log(embed = logsaiu(user.name, Role.name))
                msg_temp = await rtchannel.send(embed = logsaiu(user.name, Role.name))
                await asyncio.sleep(5)
                await msg_temp.delete()
    


#Comandos
@bot.command(pass_context=True)
async def anuncio(ctx, channel, titulo, mensagem, url):
    adms = await Adm(LideresRole, ADMSRole, PastoresRole)
    x = await check(ctx, adms)
    if x != None:
        channel = discord.utils.find(lambda x: x.position == int(channel), ctx.guild.text_channels)
        avisoschannel = bot.get_channel(channel.id)
        msg_anuncio = avisoschannel.send
        await msg_anuncio(get(avisoschannel.guild.roles, id=678449533012803596))
        await msg_anuncio(embed = anuncioembed(titulo, mensagem, url))
    else:
        await ctx.send(embed = sempermissao())


@bot.command(pass_context=True)
async def rt(ctx):
    adms = await Adm(LideresRole, ADMSRole, PastoresRole)
    x = await check(ctx, adms)
    if x != None:
        rtchannel = bot.get_channel(678453889263075349)
        await rtchannel.purge(limit = None)
        msg_temp = await rtchannel.send(embed = botreiniciando())
        await asyncio.sleep(5)
        await msg_temp.delete()
        await codcelula(rtchannel)
    else:
        await ctx.send(embed = sempermissao())

@bot.command(pass_context=True)
async def mute(ctx, channel, onoff=None):
    adms = await Adm(LideresRole, ADMSRole, PastoresRole)
    x = await check(ctx, adms)
    if x != None:
        if channel == "on" or channel == "off": 
            voicechannel = bot.get_channel(ctx.author.voice.channel.id)
        else:
            channel = discord.utils.find(lambda x: x.position == int(channel), ctx.guild.voice_channels)
            voicechannel = bot.get_channel(channel.id)
        if onoff == "on" or channel == "on":
            for user in voicechannel.members:
                verif = False
                for i in range(len(user.roles)):
                    if user.roles[i].id in adms:
                        verif = True
                if verif == False:
                    await user.edit(mute=True)
            await ctx.send(embed = muteon(voicechannel))
        elif onoff == "off" or channel == "off":
            for user in voicechannel.members:
                await user.edit(mute=False) 
            await ctx.send(embed = muteoff(voicechannel))
        else:
            await ctx.send(embed = usoincorreto())
    else:
        await ctx.send(embed = sempermissao())

@bot.command(pass_context=True)
async def move(ctx, de=None, para=None):
    adms = await Adm(LideresRole, ADMSRole, PastoresRole)
    x = await check(ctx, adms)
    if x != None:
        if de == None and para == None:
            await ctx.send(embed = usoincorreto())
        elif para == None:
            channel = bot.get_channel(ctx.author.voice.channel.id)
            channelde = discord.utils.find(lambda x: x.position == int(de), ctx.guild.voice_channels)
            channelgetde = bot.get_channel(channelde.id)

            for user in channel.members:
                await user.edit(voice_channel=channelgetde)
        else:
            channelde = discord.utils.find(lambda x: x.position == int(de), ctx.guild.voice_channels)
            channelgetde = bot.get_channel(channelde.id)

            channelpara = discord.utils.find(lambda x: x.position == int(para), ctx.guild.voice_channels)
            channelgetpara = bot.get_channel(channelpara.id)

            for user in channelgetde.members:
                await user.edit(voice_channel=channelgetpara)
    else:
        await ctx.send(embed = sempermissao())


@bot.command(pass_context=True)
async def clear(ctx, n):
    adms = await Adm(LideresRole, ADMSRole, PastoresRole)
    x = await check(ctx, adms)
    if x != None:
        if n == "all":
            msg = await ctx.channel.history(limit=None).flatten()
            await ctx.channel.purge(limit=None)
            msg_temp = await ctx.send(embed = msgclear(len(msg)))
            await asyncio.sleep(5)
            await msg_temp.delete()

        else:
            await ctx.channel.purge(limit = int(n) + 1)
            msg_temp = await ctx.send(embed = msgclear(int(n)))
            await asyncio.sleep(5)
            await msg_temp.delete()
    else:
        await ctx.send(embed = sempermissao())

@bot.command(pass_context=True)
async def disc(ctx):
    await ctx.send(embed = discor())

@bot.command(pass_context=True)
async def canaisdevoz(ctx):
    await ctx.send(embed = canalvoz(ctx))

@bot.command(pass_context=True)
async def canaisdetexto(ctx):
    await ctx.send(embed = canaltexto(ctx))

@bot.command(pass_context=True)
async def canais(ctx):
    await ctx.send(embed = canalvoz(ctx))
    await ctx.send(embed = canaltexto(ctx))

@bot.command(pass_context=True)
async def canal(ctx):
    await ctx.send(embed = canalatual(ctx))

@bot.command(pass_context=True)
async def help(ctx, *, msg):
    msg_log = logchannel.send
    ajudachanel = bot.get_channel(704739002649149652)
    
    msg_help = await ajudachanel.send(embed = helpembed(ctx, msg))
    await msg_log(embed = loghelp(ctx))
    print("Pedido de ajuda de", ctx.author, "mensagem:", msg)

    msg_temp = await ctx.send(embed = msghelp(ctx))

    await msg_help.add_reaction("✅")
    await msg_help.add_reaction("❌")

    await asyncio.sleep(10)
    await msg_temp.delete()

    reactionmsg()
    me = discord.utils.find(lambda x: x.id == 274297483696275457, msg_help.ctx.guild.members)
    if reaction.emoji == "✅":
        await msg_help.ctx.author.send(embed = resolvidomsg(msg_help.ctx))
        await msg_help.edit(embed = resolvido(msg_help.ctx, msg))
        await msg_help.remove_reaction(reaction.emoji, msg_help.author)
        await msg_help.remove_reaction(reaction.emoji, user)

    elif reaction.emoji == "❌":
        await me.send(embed = nresolvidomsg(msg_help.ctx))
        await msg_help.remove_reaction(reaction.emoji, user)
        await msg_help.remove_reaction(reaction.emoji, msg_help.author)
        await msg_help.edit(embed = nresolvido(msg_help.ctx, msg))
        await msg_help.add_reaction("✅")

@bot.command(pass_context=True)
async def privado(ctx, titulo, mensagem, url):
    adms = await Adm(LideresRole, ADMSRole, PastoresRole)
    x = await check(ctx, adms)
    if x != None:
        for guild in bot.guilds:
            for member in guild.members:
                user = bot.get_user(member.id)
                msg_anuncio = user.send
                await msg_anuncio(embed = anuncioembed(titulo, mensagem, url))
    else:
        await ctx.send(embed = sempermissao())                


@bot.command(pass_context=True)
async def comandos(ctx):
    await ctx.send(embed = comandoshelp())

bot.run("Njg2NzU0NTU5NTMxNDE3NjEx.XqSNIw.9je-13RL3Xaef4EpXnuMMsiHMM4")