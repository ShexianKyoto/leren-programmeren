import random

kleuren = ('rood', 'blauw', 'groen', 'geel', 'bruin')
hoeveelheid = int(input('''Hoeveel M&M\'s wil je toevoegen aan de zak?
'''))
zak = {
    # 'rood': 0,
    # 'blauw': 0,
    # 'groen': 0,
    # 'geel': 0,
    # 'bruin': 0,
}

for willekeurig in range(1, hoeveelheid+1):
    randomkleur = random.choice(kleuren)
    if randomkleur == 'rood': 
        if 'rood' not in zak.keys():
            zak.update({'rood': 0})
        else: zak['rood'] += 1
    if randomkleur == 'blauw':
        if 'blauw' not in zak.keys():
            zak.update({'blauw': 0})
        else: zak['blauw'] += 1
    if randomkleur == 'groen': 
        if 'groen' not in zak.keys():
            zak.update({'groen': 0})
        else: zak['groen'] += 1
    if randomkleur == 'geel':
        if 'geel' not in zak.keys():
            zak.update({'geel': 0})
        else: zak['geel'] += 1
    if randomkleur == 'bruin':
        if 'bruin' not in zak.keys():
            zak.update({'bruin': 0})
        else: zak['bruin'] += 1
print(f'Zak: {zak}')