import discord

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
    help.add_field(name = '.move', value = 'Move usuários de um canal de voz para outro. Usando apenas .move você vê a posição dos canais.\nEx: .move "de canal(posição)" "para canal(posição)"', inline = False)
        
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

def muteon(channel):
    embed = discord.Embed(
        title=f"Todos os usuários do canal |{channel}| foram MUTADOS",
        color = 0xFFFAFA
    )
    return embed

def muteoff(channel):
    embed = discord.Embed(
        title=f"Todos os usuários do canal |{channel}| foram DESMUTADOS",
        color = 0xFFFAFA
    )
    return embed

def mover(ctx):
    msg_final = ''
    for channel in ctx.guild.voice_channels:
        msg_final += f'\n{channel.position}° >>> {channel.name}'
    embed = discord.Embed(
        title = f'\tCanais de Voz',
        description = f'{msg_final}',
        color = 0xFFFAFA
    )
    return embed