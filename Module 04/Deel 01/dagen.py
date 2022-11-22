week = ('maandag','dinsdag','woensdag','donderdag','vrijdag','zaterdag','zondag')
print(f'''
Alle dagen van de week zijn: {week}
De werkdagen zijn: {week[0:5]}
De weekenddagen zijn: {week[5:7]}
Alle dagen van de week in omgekeerde volgorde zijn: {week[::-1]}
De werkdagen in omgekeerde volgorde zijn: {week[-3::-1]}
De weekenddagen in omgekeerde volgorde zijn: {week[-1:-3:-1]}
''')