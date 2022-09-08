melk = float(0.8)
bloem = int(500)
eieren = int(3)
boter = int(30)
zout = int(1)

hoeveelheid_pannenkoeken = input(f'''Hoeveel pannenkoeken wilt u maken?
Aantal: ''')
hoeveelheid =  int(hoeveelheid_pannenkoeken)
print(f'Pannenkoeken recept voor {hoeveelheid} stuks:')

melk = melk / 20 * hoeveelheid
bloem = bloem / 20 * hoeveelheid
eieren = eieren / 20 * hoeveelheid
boter = boter / 20 * hoeveelheid
zout = zout / 20 * hoeveelheid

print(f'''Melk: {melk} liter
Bloem: {bloem} gram
Eieren: {eieren} eieren
Boter: {boter} gram
Zout: {zout} teelepel''')
print('Veel kookplezier en eet smakelijk!')
