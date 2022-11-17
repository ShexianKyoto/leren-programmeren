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
    if randomkleur == 'rood': zak['rood'] += 1
    if randomkleur == 'blauw': zak['blauw'] += 1
    if randomkleur == 'groen': zak['groen'] += 1
    if randomkleur == 'geel': zak['geel'] += 1
    if randomkleur == 'bruin': zak['bruin'] += 1
print(f'Zak: {zak}')