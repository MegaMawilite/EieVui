import discord
import random
import os
from pics import *
from vees import *
from help import *

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

vees = vees()


def get_vee(v):
  i = random.randint(0, len(vees[v]) - 1)
  return (vees[v][i])


def get_reverselink(vee):
  return (
    "https://www.bing.com/images/search?view=detailv2&iss=sbi&FORM=SBIHMP&sbisrc=UrlPaste&q=imgurl:https%3A%2F%2Fi.imgur.com%2F"
    + vee + "&idpbck=1")


@client.event
async def on_ready():
  print('Logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  if message.author.bot or (not message.content.startswith('~')) or (
      message.content.startswith('~~')):
    return

  if message.content == '~hello':
    await message.channel.send("Hello! :)")
  if message.content == '~boo':
    await message.channel.send(":O")

  if message.content.startswith('~help'):
    try:
      help = message.content.split("~help ", 1)[1]
    except:
      help = ""
    await message.author.send(gethelp(help, True))

  for v in range(0, 9):
    if message.content == ('~' + vletter[v]) or (message.content == (
        '~' + vhalf[v]) or message.content == ('~' + vfull[v])):
      vee = get_vee(v)
      rl = get_reverselink(vee)
      embed = discord.Embed(title=vcapped[v] + " " + vemoji[v],
                            url='https://i.imgur.com/' + vee,
                            color=vcolor[v],
                            description="[Reverse Image Search (Bing)](" + rl +
                            ")")
      embed.set_image(url='https://i.imgur.com/' + vee)
      await message.channel.send(embed=embed)


try:
  client.run(os.environ['MY_TOKEN'])
except discord.errors.HTTPException:
  print("\n\n\nBLOCKED BY RATE LIMITS\nRESTARTING NOW\n\n\n")
  os.system("python restarter.py")
  os.system('kill 1')
