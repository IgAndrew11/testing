import discord
from discord.ext import commands

Token='MTI1NTkxMTM5MjQwMjIxNDk0Mw.Ga0Rb2.V7ksRbgJLqlhLC3TpuAuId_JS8_GP5lDKYWny0'



intents = discord.Intents.all()


bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user},{bot.user.id}')
    print('----------------------------------------------------------------------------------')
    print('bot Running :')
    print('----------------------------------------------------------------------------------')
   
    print('----------------------------------------------------------------------------------')
    print('bot Running :Online ')
    print('----------------------------------------------------------------------------------')

    print('----------------------------------------------------------------------------------')
    print('bot Running : ')
    print('----------------------------------------------------------------------------------')

@bot.command()
async def hello(ctx):
    await ctx.send('Hello!')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')
''''
@bot.command()
async def sendembed(ctx):
    embeded_msg = discord.Embed(title="discord",description="enter your discription ",color=discord.Color.blue())
    embeded_msg.set_thumbnail(url = ctx.author.avatar)
    embeded_msg.add_field(name="enter you name ",value="ente the val;ue ",inline=False)
    embeded_msg.set_image(url=ctx.guild.avatar)
    embeded_msg.set_footer(text="foooter text nmame or ",icon_url=ctx.author.avatar)
    await ctx.send(embed=embeded_msg)

'''
@bot.event
async def on_member_join(member):
    member_tag =( f'{member.name}#{member.discriminator}')
    print(f'{member_tag} has joined the server.')
    channel = bot.get_channel(1173589118685544528 )
    if channel:
       await channel.send(f'Welcome {member_tag} {member.mention} to the server!')

@bot.command()

async def sendembed(ctx):
             
        embed_msg = discord.Embed(title="Welcome",description=f"#  This is an example embed.",color=discord.Color.green()) 
        embed_msg.add_field(name="louie Andrew ",value=f'<#1173589131654348892>')
        embed_msg.add_field( name=  "louie Andrew  ",
                            value="ente the val;ue ",
                            inline=False)
        embed_msg.set_thumbnail(url = ctx.author.avatar)
        embed_msg.set_image(url="https://cdn.discordapp.com/attachments/1173629723734183936/1264266997974175854/welcome_GIF_-_Find__Share_on_GIPHY.gif?ex=669d3fe5&is=669bee65&hm=2c41b74b210eebfc5869f1ee90475eea75c1d02b92ba9b2e4be3feec2bc21027&")
        await ctx.send(embed=embed_msg)
    

   
@bot.event
async def on_member_join(member):
    member_tag =( f'{member.name}#{member.discriminator}')
    print(f'{member_tag} has joined the server.')
    channel = bot.get_channel(1173589118685544528 )
    if channel:
       await channel.send(f'Welcome {member_tag} {member.mention} to the server!')
       
 
bot.run(Token)
