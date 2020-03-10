import discord
from discord.utils import get

bot = discord.Client()
@bot.event
async def on_ready():
    print('bot online')

@bot.event
async def on_message(message):
    if message.content.lower().startswith("?r"):
        
        global EkklesiaRole
        EkklesiaID = 678462920862072852
        EkklesiaRole = get(message.guild.roles, id=EkklesiaID)

        global JudahRole
        JudahID = 678463157374550017
        JudahRole = get(message.guild.roles, id=JudahID)

        global MaanaimRole
        MaanaimID = 678463077003427841
        MaanaimRole = get(message.guild.roles, id=MaanaimID)

        global AhavaRole
        AhavaID = 678463327793446913
        AhavaRole = get(message.guild.roles, id=AhavaID)

        global EliteRole
        EliteID = 678463392255705109
        EliteRole = get(message.guild.roles, id=EliteID)

        global TeknongramosRole
        TeknongramosID = 678463256460787732
        TeknongramosRole = get(message.guild.roles, id=TeknongramosID)

        global HovhanessRole
        HovhanessID = 678467646269685761
        HovhanessRole = get(message.guild.roles, id=HovhanessID)

        global NullRole
        NullID = 686764850416058378
        NullRole = get(message.guild.roles, id=NullID)


        escolhercelula = discord.Embed(
            title = "Seleciona a sua Célula:",
            color = 0x22a7f0
        )
        escolhercelula.add_field(name = "Ekklesia", value = ":zero:", inline = True)
        escolhercelula.add_field(name = "Hovhaness", value = ":one:", inline = True)
        escolhercelula.add_field(name = "Teknongramos", value = ":two:", inline = True)
        escolhercelula.add_field(name = "Judah", value = ":three:", inline = True)
        escolhercelula.add_field(name = "Maanaim", value = ":four:", inline = True)
        escolhercelula.add_field(name = "Elite", value = ":five:", inline = True)
        escolhercelula.add_field(name = "Ahava", value = ":six:", inline = True)
        escolhercelula.add_field(name = "Null", value = ":seven:", inline = True)
        global msg_bot
        msg_bot = await message.channel.send(embed = escolhercelula)

        await msg_bot.add_reaction("0️⃣")
        await msg_bot.add_reaction("1️⃣")
        await msg_bot.add_reaction("2️⃣")
        await msg_bot.add_reaction("3️⃣")
        await msg_bot.add_reaction("4️⃣")
        await msg_bot.add_reaction("5️⃣")
        await msg_bot.add_reaction("6️⃣")
        await msg_bot.add_reaction("7️⃣")

@bot.event
async def on_reaction_add(reaction, user):
    celulas = [EkklesiaRole.id, JudahRole.id, MaanaimRole.id, AhavaRole.id, EliteRole.id, TeknongramosRole.id, HovhanessRole.id, NullRole.id]
    ncelulas = [679059732119683083, 678450377678651392, 678463459385540618, 678449533012803596]
    if msg_bot.id == reaction.message.id and user.name != "RadicalTeenBot":
        verif = True
        for i in range(len(user.roles)):
            if user.roles[i].id in celulas:
                verif = False

        if verif:
            if reaction.emoji == "0️⃣":
                await user.add_roles(EkklesiaRole)
            elif reaction.emoji == "1️⃣":
                await user.add_roles(JudahRole)
            elif reaction.emoji == "2️⃣":
                await user.add_roles(MaanaimRole)
            elif reaction.emoji == "3️⃣":
                await user.add_roles(AhavaRole)
            elif reaction.emoji == "4️⃣":
                await user.add_roles(EliteRole)
            elif reaction.emoji == "5️⃣":
                await user.add_roles(TeknongramosRole)
            elif reaction.emoji == "6️⃣":
                await user.add_roles(HovhanessRole)
            elif reaction.emoji == "7️⃣":
                await user.add_roles(NullRole)

@bot.event
async def on_reaction_remove(reaction, user):
    if reaction.emoji == "0️⃣":
        verif = True
        for i in range(len(user.roles)):
            if user.roles[i].id == EkklesiaRole.id:
                verif = False
        if not verif:
            await user.remove_roles(EkklesiaRole)       
    
    if reaction.emoji == "1️⃣":
        verif = True
        for i in range(len(user.roles)):
            if user.roles[i].id == JudahRole.id:
                verif = False
        if not verif:
            await user.remove_roles(JudahRole)      

    if reaction.emoji == "2️⃣":
        verif = True
        for i in range(len(user.roles)):
            if user.roles[i].id == MaanaimRole.id:
                verif = False
        if not verif:
            await user.remove_roles(MaanaimRole)
    
    if reaction.emoji == "3️⃣":
        verif = True
        for i in range(len(user.roles)):
            if user.roles[i].id == AhavaRole.id:
                verif = False
        if not verif:
            await user.remove_roles(AhavaRole)
    
    if reaction.emoji == "4️⃣":
        verif = True
        for i in range(len(user.roles)):
            if user.roles[i].id == EliteRole.id:
                verif = False
        if not verif:
            await user.remove_roles(EliteRole)
    
    if reaction.emoji == "5️⃣":
        verif = True
        for i in range(len(user.roles)):
            if user.roles[i].id == TeknongramosRole.id:
                verif = False
        if not verif:
            await user.remove_roles(TeknongramosRole)
    
    if reaction.emoji == "6️⃣":
        verif = True
        for i in range(len(user.roles)):
            if user.roles[i].id == HovhanessRole.id:
                verif = False
        if not verif:
            await user.remove_roles(HovhanessRole)
    
    if reaction.emoji == "7️⃣":
        verif = True
        for i in range(len(user.roles)):
            if user.roles[i].id == NullRole.id:
                verif = False
        if not verif:
            await user.remove_roles(NullRole)
    

bot.run('Njg2NzU0NTU5NTMxNDE3NjEx.Xmb0JQ.yzKqYeoKlX93FKGXTAp2ViVw9fI')