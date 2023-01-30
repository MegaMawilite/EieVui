import discord
import random
import os
from replit import db
from pics import *
from vees import *
from help import *
from evdays import *

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

vees = vees()

db["suggclear"] = 0


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
  if message.author == await client.fetch_user(os.environ['MAWS_ID']):
    if message.content == "y" and db["suggclear"] == 1:
      db["sugs"] = "SUGGESTIONS:"
      await message.author.send("Suggestions all cleared.")
    db["suggclear"] = 0

  if message.author.bot or (not message.content.startswith('~')) or (
      message.content.startswith('~~')):
    return

  # vee pics
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

  # vee days
  if message.content == '~cal' or message.content == '~calendar':
    cal = get_cal()
    await message.channel.send(embed=cal)
  if message.content == '~when':
    await message.channel.send(get_when())

  # simple misc
  if message.content == '~hello':
    await message.channel.send("Hello! :)")
  if message.content == '~boo':
    await message.channel.send(":O")

  # help
  if message.content.startswith('~help'):
    try:
      help = message.content.split("~help ", 1)[1]
    except:
      help = ""
    await message.author.send(gethelp(help, True))

  # bug feedback
  if message.content.startswith('~bug'):
    try:
      bugmsg = message.content.split("~bug ", 1)[1]
      try:
        maw = await client.fetch_user(os.environ['MAWS_ID'])
        err = 0
      except:
        err = 1
        errmsg = "Uh oh. I couldn't find my creator's ID..."
    except:
      err = 1
      errmsg = "The feedback cannot be empty."
    if err == 1:
      await message.channel.send(errmsg)
    else:
      await maw.send(bugmsg)
      await message.channel.send("Feedback sent successfully.")

  # suggestion feedback
  if message.content.startswith('~suggest'):
    try:
      sugs = db["sugs"]
    except:
      sugs = "SUGGESTIONS:"
      db["sugs"] = sugs
    if message.author == await client.fetch_user(os.environ['MAWS_ID']):
      if message.content == '~suggest clear':
        db["suggclear"] = 1
        await message.author.send("Are you sure? (y/n)")
      else:
        await message.author.send(sugs)
    else:
      try:
        sugmsg = message.content.split("~suggest ", 1)[1]
        err = 0
      except:
        err = 1
        errmsg = "The feedback cannot be empty."
      if err == 1:
        await message.channel.send(errmsg)
      else:
        sugs = sugs + "\n" + sugmsg
        db["sugs"] = sugs
        await message.channel.send("Feedback sent successfully.")


try:
  client.run(os.environ['MY_TOKEN'])
except discord.errors.HTTPException:
  print("\n\n\nBLOCKED BY RATE LIMITS\nRESTARTING NOW\n\n\n")
  os.system("python restarter.py")
  os.system('kill 1')
