import random

kleuren = ('rood', 'blauw', 'groen', 'geel', 'bruin')
hoeveelheid = int(input('''Hoeveel M&M\'s wil je toevoegen aan de zak?
'''))
zak = {
    'rood': 0,
    'blauw': 0,
    'groen': 0,
    'geel': 0,
    'bruin': 0,
}

for willekeurig in range(1, hoeveelheid+1):
    randomkleur = random.choice(kleuren)
    if randomkleur == 'rood': zak.update({'rood': +1})
print(f'Zak: {zak}')