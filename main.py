import discord
import random
import asyncio
from discord.utils import get
from discord.ext import commands

bot = commands.Bot(command_prefix = '.')
testechannel = bot.get_channel(686763964256092164)
rtchannel = bot.get_channel(678453889263075349)


#Funções LOG
def logentrou(nome, celula):
    log = discord.Embed(
        title = f"{nome} entrou em {celula}",
        color = 0x008000
    )
    return log

def logsaiu(nome, celula):
    log = discord.Embed(
        title = f"{nome} saiu de {celula}",
        color = 0xFF0000
    )
    return log



#Função Escolher Celula
def escolhercelula():
    escolhercelula = discord.Embed(
        title = "Seleciona a sua Célula:",
        color = 0xFFFAFA
    )
    escolhercelula.add_field(name = "🦁 Ekklesia", value = ":zero:", inline = True)
    escolhercelula.add_field(name = "🦅 Hovhaness", value = ":one:", inline = True)
    escolhercelula.add_field(name = "🌲 Teknongramos", value = ":two:", inline = True)
    escolhercelula.add_field(name = "🦁 Judah", value = ":three:", inline = True)
    escolhercelula.add_field(name = "🐺 Maanaim", value = ":four:", inline = True)
    escolhercelula.add_field(name = "🦅 Elite", value = ":five:", inline = True)
    escolhercelula.add_field(name = "🧡 Ahava", value = ":six:", inline = True)
    '''escolhercelula.add_field(name = "Makarias", value = ":seven:", inline = True)'''

    return escolhercelula

#Comandos
def help():
    help = discord.Embed(
        title = f"Comandos",
        color = 0xFFFAFA
    )

    help.add_field(name = '.anuncio', value = 'Faz anúncios com o bot.\nEx: .anuncio "Titulo" "Mensagem" Url', inline = False)
    help.add_field(name = '.r', value = 'Aparece um novo bloco de escolher celula.\nEx: .r', inline = False)
    help.add_field(name = '.mute', value = 'Silencia ou "diselencia" o canal de voz inteiro em que você está.\nEx: .mute on/off', inline = False)
        
    return help

def anuncioembed(titulo, mensagem, url):
    anuncio = discord.Embed(
        title = f"{titulo}",
        color = 0xFF0000,
        description = f"{mensagem}",
    url=url).set_image(url=url)
    return anuncio




#Mensagens e erros
def possuicelula(nome):
    possuicelula = discord.Embed(
            title = f"{nome}, você já está em outra célula. Só é possível estar em uma de cada vez.",
            color = 0xFFFAFA
    )
    
    return possuicelula

def mesmacelula(nome):
    mesmacelula = discord.Embed(
            title = f"{nome}, você já está nessa célula. Para sair dela, clique novamente.",
            color = 0xFFFAFA
    )

    return mesmacelula

def bemvindo(user):
    bemvindo = discord.Embed(
        title = f"{user.name}, Bem-Vindo ao discord do Radical Teen. Selecione a sua célula",
        color = 0xFFFAFA
    )
    return bemvindo

def sempermissao():
    embed = discord.Embed(
        title = f"Você não tem permissão para usar esse comando.",
        color = 0xFF0000
    )
    return embed

def zoom(user):
    embed = discord.Embed(
        title = f"Na Na Ni Na Não, {user}!\nEspalhe o discord para a galera:\nhttps://discord.gg/AR3mQbQ",
        color = 0xFF0000
    )
    return embed

def usoincorreto():
    embed = discord.Embed(
        title=f"Comando usado de forma incorreta. Para mais informações tente .comandos",
        color = 0xFF0000
    )
    return embed



async def clear(n):
    rtchannel = bot.get_channel(678453889263075349)
    await rtchannel.purge(limit = n)



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
    EveryoneID = 678449533012803596
    EveryoneRole = get(rtchannel.guild.roles, id=EveryoneID)

    global RadicalTeenRole
    RadicalTeenID = 678463459385540618
    RadicalTeenRole = get(rtchannel.guild.roles, id=RadicalTeenID)

    global LideresRole
    LideresRoleID = 678450377678651392
    LideresRole = get(rtchannel.guild.roles, id=LideresRoleID)

    global ADMSRole
    ADMSID = 679059732119683083
    ADMSRole = get(rtchannel.guild.roles, id=ADMSID)

    global PastoresRole
    PastoresID = 689875778858385467
    PastoresRole = get(rtchannel.guild.roles, id=PastoresID)


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
    print('Bot on')

    await clear(100)

    await codigo()

    



@bot.event
async def on_member_join(user):
    await user.add_roles(RadicalTeenRole)

    await clear(100)

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
            Role = NullRole
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
        await clear(100)
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