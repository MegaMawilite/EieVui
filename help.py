def gethelp(h, first):
  if first == True:
    greetings = "Here to help!"
  else:
    greetings = "Sorry, this category number doesn't exist..."
  if h == "":  #main
    return (greetings + '''
    
**__`EieVui V1.0.1`__**
```
Written by Mawilite#3873. Hosted on Repl.it.
    
Commands are separated in several categories.

    
~help 1 → Eeveelution imagery commands
~help 2 → Eeveelution community day commands
~help 3 → Miscellaneous commands
    
~help 4 → Feedback commands
    

...and more commands to come in the future!```
''')
  elif h == "1":
    return ('''
My main purpose!

**__`Eeveelution imagery commands`__**
```
Returns a random image from the specified eeveelution, along with a reverse image search link.
    

~eevee ~vee ~e ─────→ Eevee
~vaporeon ~vapor ~v → Vaporeon
~jolteon ~jolt ~j ──→ Jolteon
~flareon ~flar ~f ──→ Flareon
~espeon ~esp ~p ────→ Espeon
~umbreon ~umbr ~u ──→ Umbreon
~leafeon ~leaf ~l ──→ Leafeon
~glaceon ~glac ~g ──→ Glaceon
~sylveon ~sylv ~s ──→ Sylveon```
''')
  elif h == "2":
    return ('''
Let's celebrate!

**__`Eeveelution community day commands`__**
```
Commands related to eeveelution community days.
    

~when
 └→ Returns how many days remains before the next community day.
     
~calendar ~cal
 └→ Returns the list of all eeveelution community days.```
''')
  elif h == "3":
    return ('''
Just random stuff!

**__`Miscellaneous commands`__**
```
Commands that do not fit in any other category.
    

~hello 
~boo```
''')
  elif h == "4":
    return ('''
Any idea or issue?

**__`Feedback commands`__**
```
Sends feedback to the creator.

/!\ Please only use ~bug for bugs and issues.
/!\ Please don't spam.
/!\ Please stay civil and use common sense.
Failing to do so might result in removal of BOTH commands of the category.
    

~bug [message]
 └→ Sends [message] as a DM to the creator.
    
~suggest [message]
 └→ Saves [message]. The creator can access those messages anytime whenever she wants to improve me.```
''')
  else:
    return (gethelp("", False))
