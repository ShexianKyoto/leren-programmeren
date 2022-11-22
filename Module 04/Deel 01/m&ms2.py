import random

kleuren = ('rood', 'blauw', 'groen', 'geel', 'bruin')
hoeveelheid = int(input('''Hoeveel M&M\'s wil je toevoegen aan de zak?
'''))
zak = {}

for randomk in range(hoeveelheid):
    randomkleur = random.choice(kleuren)
    if randomkleur not in zak: zak.update({randomkleur: 1})
    else: zak[randomkleur] += 1
print(f'Zak: {zak}')