import time
import discord
from vees import *

dates = [326, 338, 72, 10, 234, 38, 170, 245, 52, "", "", "", 366 + 10]
order = [3, 5, 8, 2, 6, 4, 7, 0, 1, 12]
fulldates = [
  "January 10", "February 7", "February 21", "March 12", "June 18",
  "August 21", "September 1", "November 21", "December 3"
]
# the extra date and the "12" is for flareon's to be calculated correctly over the new year (12 mod 9 = 3)


def get_next_evday():
  d = int(time.strftime("%j", time.localtime()))
  y = int(time.strftime("%y", time.localtime()))
  if d > dates[8] and y % 4 != 0:
    leap = 1
  else:
    leap = 0
  ev = 0
  found = False
  while not found:
    if (d + leap) > dates[order[ev]]:
      ev += 1
    else:
      found = True
  return [order[ev] % 9, dates[order[ev]] - (d + leap)]


def get_cal_desc(next, now):
  desc = ""
  for i in range(0, 9):
    if next == order[i]:
      desc = desc + "**__"
    desc = desc + vemoji[order[i]] + vcapped[order[i]] + ": " + fulldates[i]
    if next == order[i]:
      if now:
        desc = desc + " (TODAY!)"
      else:
        desc = desc + " (Next)"
      desc = desc + "__**"
    if i < 9:
      desc = desc + "\n"
  return desc


def get_cal():
  ev = get_next_evday()[0]
  til = get_next_evday()[1]
  date = time.strftime("%B %d", time.localtime())
  desc = get_cal_desc(ev, til == 0)
  embed = discord.Embed(title=date, color=vcolor[ev], description=desc)
  embed.set_author(name="Today is")
  return embed


def get_when():
  ev = get_next_evday()[0]
  til = get_next_evday()[1]
  if til == 0:
    return (vemoji[ev] + vemoji[ev] + vemoji[ev] + " IT'S " + vcapped[ev] +
            " DAY!🎉 " + vemoji[ev] + vemoji[ev] + vemoji[ev])
  elif til == 1:
    return (vemoji[ev] + " " + vcapped[ev] + " day is tomorrow! " + vemoji[ev])
  else:
    return (vemoji[ev] + " " + vcapped[ev] + " day is in " + str(til) +
            " days! " + vemoji[ev])
