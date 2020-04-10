import discord
import random
import asyncio
from time import strftime, localtime, time
from datetime import datetime
from discord.utils import get
from discord.ext import commands
from utility import *

bot = commands.Bot(command_prefix = '.')
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

async def codigo(rtchannel):


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
    print(strftime("%A, %d/%m/%Y %H:%M:%S", localtime(time()-10800)),'\n Iniciando Bot...')
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("Radical Teen ✝"))
    rtchannel = bot.get_channel(678453889263075349)

    await rtchannel.purge(limit = 100)

    await RoleCelulas(rtchannel)
    await AdmsRoles(rtchannel)
    await codigo(rtchannel)



@bot.event
async def on_member_join(user):
    rtchannel = bot.get_channel(678453889263075349)

    if str(user.bot) == "False":
        await rtchannel.purge(limit = 100)

        await user.add_roles(get(rtchannel.guild.roles, id=678463459385540618))

        msg_temp = await rtchannel.send(f'<@!{user.id}>')
        msg_temp2 = await rtchannel.send(embed = bemvindo(user))

        await codigo(rtchannel)

        await asyncio.sleep(30)
        await msg_temp.delete()
        await msg_temp2.delete()


'''
@bot.event
async def on_member_update(before, after):
    botteste = 688243571865682010
    if after.id == botteste:
        if str(before.status) == "online" and str(after.status) == "offline":
            rtchannel = bot.get_channel(678453889263075349)
            await rtchannel.purge(limit = 100)
            msg_temp = await rtchannel.send(embed = botreiniciando())
            await asyncio.sleep(5)
            await msg_temp.delete()
            await codigo(rtchannel)
'''


@bot.event
async def on_message(message):
    message_content = message.content.strip().lower()
    if "zoom" in message_content:
        user = message.author.name
        channel = bot.get_channel(message.channel.id)
        await message.delete()
        msg_temp = await channel.send(embed = zoom(user))
        await asyncio.sleep(15)
        await msg_temp.delete() 

    if "discord" in message_content:
        channel = bot.get_channel(message.channel.id)
        await asyncio.sleep(15)
        await channel.send(embed = discor1())

      


    await bot.process_commands(message) #ISSO FAZ OS COMANDOS FUNCIONAREM


@bot.event
async def on_reaction_add(reaction, user):
    rtchannel = bot.get_channel(678453889263075349)
    if msg_bot.id == reaction.message.id and user.name != msg_bot.author.name:

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


@bot.event
async def on_reaction_remove(reaction, user):
    rtchannel = bot.get_channel(678453889263075349)
    if msg_bot.id == reaction.message.id:
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
async def anuncio(ctx, titulo, mensagem, url):
    adms = await Adm(LideresRole, ADMSRole, PastoresRole)
    x = await check(ctx, adms)
    if x != None:  
        global avisoschannel
        avisoschannel = bot.get_channel(697951710764859392)
        msg_anuncio = avisoschannel.send
        await msg_anuncio(get(rtchannel.guild.roles, id=678449533012803596))
        await msg_anuncio(embed = anuncioembed(titulo, mensagem, url))
    else:
        await ctx.send(embed = sempermissao())


@bot.command(pass_context=True)
async def r(ctx):
    adms = await Adm(LideresRole, ADMSRole, PastoresRole)
    x = await check(ctx, adms)
    if x != None:
        rtchannel = bot.get_channel(678453889263075349)
        await rtchannel.purge(limit = 100)
        msg_temp = await rtchannel.send(embed = botreiniciando())
        await asyncio.sleep(5)
        await msg_temp.delete()
        await codigo(rtchannel)
    else:
        await ctx.send(embed = sempermissao())

@bot.command(pass_context=True)
async def mute(ctx, channel, onoff=None):
    adms = await Adm(LideresRole, ADMSRole, PastoresRole)
    x = await check(ctx, adms)
    if x != None:
        channel = discord.utils.find(lambda x: x.position == int(channel), ctx.guild.voice_channels)
        voicechannel = bot.get_channel(channel.id)
        if onoff == "on":
            for user in voicechannel.members:
                verif = True
                for i in range(len(user.roles)):
                    if user.roles[i].id in adms:
                        verif = False
                if verif:
                    await user.edit(mute=True)  
            msg_temp = await ctx.send(embed = muteon(voicechannel))
            await asyncio.sleep(5)
            await msg_temp.delete()  
        elif onoff == "off":
            for user in voicechannel.members:
                await user.edit(mute=False) 
            msg_temp = await ctx.send(embed = muteoff(voicechannel))
            await asyncio.sleep(5)
            await msg_temp.delete()
        else:
            await ctx.send(embed = usoincorreto())
    else:
        await ctx.send(embed = sempermissao())

@bot.command(pass_context=True)
async def move(ctx, de=None, para=None):
    adms = await Adm(LideresRole, ADMSRole, PastoresRole)
    x = await check(ctx, adms)
    if x != None:
        if de == None or para == None:
            await ctx.send(embed = usoincorreto())
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
async def canais(ctx):
    await ctx.send(embed = mover(ctx))


'''
@bot.command(pass_context=True)
async def teste(ctx):
    adms = await Adm(LideresRole, ADMSRole, PastoresRole)
    x = check(ctx, adms)
    if x != None:
        print("adm")
    else:
        print("nao é adm")
'''

@bot.command(pass_context=True)
async def comandos(ctx):
    await ctx.send(embed = help())


#bot teste
bot.run('Njg4MjQzNTcxODY1NjgyMDEw.Xmxgqw.XhjuH_MD00rNAJf9ZTjKuqSlzcs')

#bot normal
#bot.run('Njg2NzU0NTU5NTMxNDE3NjEx.XmcVXQ.JlCDQUiBkgFVw8-hqmMELI4IoRw')