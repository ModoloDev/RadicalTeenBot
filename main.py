import discord
import random
import asyncio
from discord.utils import get
from discord.ext import commands

bot = commands.Bot(command_prefix = '.')
testechannel = bot.get_channel(686763964256092164)


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
    '''escolhercelula.add_field(name = "Null", value = ":seven:", inline = True)'''

    return escolhercelula

#Comandos
def help():
    help = discord.Embed(
        title = f"Comandos",
        color = 0xFFFAFA
    )

    help.add_field(name = '.anuncio', value = 'Faz anúncios com o bot.\nEx: .anuncio "Titulo" "Mensagem" Url', inline = False)
    help.add_field(name = '.r', value = 'Aparece um novo bloco de escolher celula.\nEx: .r', inline = False)
        
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







@bot.event
async def on_ready():
    print('Tudo funcionando')

    global rtchannel
    rtchannel = bot.get_channel(678453889263075349)


    #Clear
    await rtchannel.purge(limit=100)

    



    global EkklesiaRole
    EkklesiaID = 678462920862072852
    EkklesiaRole = get(rtchannel.guild.roles, id=EkklesiaID)

    global JudahRole
    JudahID = 678463157374550017
    JudahRole = get(rtchannel.guild.roles, id=JudahID)

    global MaanaimRole
    MaanaimID = 678463077003427841
    MaanaimRole = get(rtchannel.guild.roles, id=MaanaimID)

    global AhavaRole
    AhavaID = 678463327793446913
    AhavaRole = get(rtchannel.guild.roles, id=AhavaID)

    global EliteRole
    EliteID = 678463392255705109
    EliteRole = get(rtchannel.guild.roles, id=EliteID)

    global TeknongramosRole
    TeknongramosID = 678463256460787732
    TeknongramosRole = get(rtchannel.guild.roles, id=TeknongramosID)

    global HovhanessRole
    HovhanessID = 678467646269685761
    HovhanessRole = get(rtchannel.guild.roles, id=HovhanessID)

    '''global NullRole
    NullID = 686764850416058378
    NullRole = get(rtchannel.guild.roles, id=NullID)'''



    global EveryoneRole
    EveryoneID = 678449533012803596
    EveryoneRole = get(rtchannel.guild.roles, id=EveryoneID)

    global RadicalTeenRole
    RadicalTeenID = 678463459385540618
    RadicalTeenRole = get(rtchannel.guild.roles, id=RadicalTeenID)







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
async def on_member_join(user):
    await user.add_roles(RadicalTeenRole)

    selecionarcelula = asyncio.create_task(on_ready())
    await selecionarcelula

    msg_temp = await rtchannel.send(f'<@!{user.id}>')
    msg_temp2 = await rtchannel.send(embed = bemvindo(user))


    await asyncio.sleep(30)
    await msg_temp.delete()
    await msg_temp2.delete()
    


@bot.event
async def on_reaction_add(reaction, user):
    celulas = [EkklesiaRole.id, JudahRole.id, MaanaimRole.id, AhavaRole.id, EliteRole.id, TeknongramosRole.id, HovhanessRole.id] #, NullRole.id]
    if msg_bot.id == reaction.message.id and user.name != msg_bot.author.name:
        verif = True
        for i in range(len(user.roles)):
            if user.roles[i].id in celulas:
                verif = False

        if verif:
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
            
            await user.add_roles(Role)
            await msg_log(embed = logentrou(user.name, Role.name))
            msg_temp = await rtchannel.send(embed = logentrou(user.name, Role.name))
            await asyncio.sleep(5)
            await msg_temp.delete()

        
        else:
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
    
    global avisoschannel
    avisoschannel = bot.get_channel(678458511780347914)
    msg_anuncio = avisoschannel.send
    await msg_anuncio(EveryoneRole)
    await msg_anuncio(embed = anuncioembed(titulo, mensagem, url))


@bot.command(pass_context=True)
async def r(ctx):
    selecionarcelula = asyncio.create_task(on_ready())
    await selecionarcelula

@bot.command(pass_context=True)
async def comandos(ctx):
    await ctx.send(embed = help())


#bot teste
#bot.run('Njg4MjQzNTcxODY1NjgyMDEw.Xmxgqw.XhjuH_MD00rNAJf9ZTjKuqSlzcs')

#bot normal
bot.run('Njg2NzU0NTU5NTMxNDE3NjEx.XmcVXQ.JlCDQUiBkgFVw8-hqmMELI4IoRw')