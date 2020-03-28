import discord
import random
import asyncio
from discord.utils import get
from discord.ext import commands
from utility import *

bot = commands.Bot(command_prefix = '.')
testechannel = bot.get_channel(686763964256092164)
rtchannel = bot.get_channel(678453889263075349)



async def codigo():
    rtchannel = bot.get_channel(678453889263075349)

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

    '''global MakariasRole
    MakariasRole = get(rtchannel.guild.roles, id=686764850416058378)'''



    global EveryoneRole
    EveryoneRole = get(rtchannel.guild.roles, id=678449533012803596)

    global RadicalTeenRole
    RadicalTeenRole = get(rtchannel.guild.roles, id=678463459385540618)

    global LideresRole
    LideresRole = get(rtchannel.guild.roles, id=678450377678651392)

    global ADMSRole
    ADMSRole = get(rtchannel.guild.roles, id=679059732119683083)

    global PastoresRole
    PastoresRole = get(rtchannel.guild.roles, id=689875778858385467)


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






@bot.event
async def on_ready():
    rtchannel = bot.get_channel(678453889263075349)
    print('Bot on')

    await rtchannel.purge(limit = 100)

    await codigo()



@bot.event
async def on_member_join(user):
    rtchannel = bot.get_channel(678453889263075349)
    await rtchannel.purge(limit = 100)

    await user.add_roles(get(rtchannel.guild.roles, id=678463459385540618))

    msg_temp = await rtchannel.send(f'<@!{user.id}>')
    msg_temp2 = await rtchannel.send(embed = bemvindo(user))

    await codigo()

    await asyncio.sleep(30)
    await msg_temp.delete()
    await msg_temp2.delete()


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
      


    await bot.process_commands(message) #ISSO FAZ OS COMANDOS FUNCIONAREM


@bot.event
async def on_reaction_add(reaction, user):
    rtchannel = bot.get_channel(678453889263075349)
    celulas = [EkklesiaRole.id, JudahRole.id, MaanaimRole.id, AhavaRole.id, EliteRole.id, TeknongramosRole.id, HovhanessRole.id] #, NullRole.id]
    if msg_bot.id == reaction.message.id and user.name != msg_bot.author.name:
        verif = True
        for i in range(len(user.roles)):
            if user.roles[i].id in celulas:
                verif = False

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

        if verif:
            await user.add_roles(Role)
            await msg_log(embed = logentrou(user.name, Role.name))
            msg_temp = await rtchannel.send(embed = logentrou(user.name, Role.name))
            await asyncio.sleep(5)
            await msg_temp.delete()        
        else:
            verif = True
            for i in range(len(user.roles)):
                if user.roles[i].id == Role.id:
                    verif = False
            if not verif:
                msg_temp = await rtchannel.send(embed = mesmacelula(user.name))
                msg_temp
                await asyncio.sleep(5)
                await msg_temp.delete()
            else:
                msg_temp = await rtchannel.send(embed = possuicelula(user.name))
                msg_temp
                await asyncio.sleep(5)
                await msg_temp.delete()


@bot.event
async def on_reaction_remove(reaction, user):
    rtchannel = bot.get_channel(678453889263075349)
    if msg_bot.id == reaction.message.id:

        verif = True
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
        
        for i in range(len(user.roles)):
            if user.roles[i].id == Role.id:
                verif = False
        if not verif:
            await user.remove_roles(Role)  
            await msg_log(embed = logsaiu(user.name, Role.name))
            msg_temp = await rtchannel.send(embed = logsaiu(user.name, Role.name))
            msg_temp
            await asyncio.sleep(5)
            await msg_temp.delete()
    



@bot.command(pass_context=True)
async def anuncio(ctx, titulo, mensagem, url):
    adms = [ADMSRole.id, LideresRole.id, PastoresRole.id]
    verif = True
    for i in range(len(ctx.author.roles)):
        if ctx.author.roles[i].id in adms:
            verif = False
    if not verif:   
        global avisoschannel
        avisoschannel = bot.get_channel(678458511780347914)
        msg_anuncio = avisoschannel.send
        await msg_anuncio(EveryoneRole)
        await msg_anuncio(embed = anuncioembed(titulo, mensagem, url))
    else:
        await ctx.send(embed = sempermissao())


@bot.command(pass_context=True)
async def r(ctx):
    adms = [ADMSRole.id, LideresRole.id, PastoresRole.id]
    verif = True
    for i in range(len(ctx.author.roles)):
        if ctx.author.roles[i].id in adms:
            verif = False
    if not verif:
        await rtchannel.purge(limit = 100)
        await codigo()
    else:
        await ctx.send(embed = sempermissao())

@bot.command(pass_context=True)
async def mute(ctx, onoff):
    adms = [ADMSRole.id, LideresRole.id, PastoresRole.id]
    verif = True
    for i in range(len(ctx.author.roles)):
        if ctx.author.roles[i].id in adms:
            verif = False
    if not verif:
        voicechannel = bot.get_channel(ctx.author.voice.channel.id)
        if onoff == "on":
            for user in voicechannel.members:
                verif = True
                for i in range(len(user.roles)):
                    if user.roles[i].id in adms:
                        verif = False
                if verif:
                    await user.edit(mute=True)    
        elif onoff == "off":
            for user in voicechannel.members:
                await user.edit(mute=False)
        else:
            await ctx.send(embed = usoincorreto())
    else:
        await ctx.send(embed = sempermissao())

@bot.command(pass_context=True)
async def comandos(ctx):
    await ctx.send(embed = help())


#bot teste
#bot.run('Njg4MjQzNTcxODY1NjgyMDEw.Xmxgqw.XhjuH_MD00rNAJf9ZTjKuqSlzcs')

#bot normal
bot.run('Njg2NzU0NTU5NTMxNDE3NjEx.XmcVXQ.JlCDQUiBkgFVw8-hqmMELI4IoRw')