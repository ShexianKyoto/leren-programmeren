fruitmand = [{
    'name' : 'ananas',
    'weight' : 1590,
    'color' : 'yellow',
    'round' : False
},{
    'name' : 'appel',
    'weight' : 195,
    'color' : 'green',
    'round' : True
},{
    'name' : 'sinaasappel',
    'weight' : 130,
    'color' : 'orange',
    'round' : True
},{
    'name' : 'banaan',
    'weight' : 120,
    'color' : 'yellow',
    'round' : False
},{
    'name' : 'druif',
    'weight' : 5,
    'color' : 'red',
    'round' : True
},{
    'name' : 'kiwi',
    'weight' : 75,
    'color' : 'brown',
    'round' : False
},{
    'name' : 'citroen',
    'weight' : 100,
    'color' : 'yellow',
    'round' : True
}]
for i in fruitmand:
    naam = i['name']
    lengte = len(i['name'])
    kleur = i['color']
    if kleur == 'yellow': kleur = 'gele' #geel groen oranje rood bruin
    elif kleur == 'green': kleur = 'groene'
    elif kleur == 'orange': kleur = 'oranje'
    elif kleur == 'red': kleur = 'rode'
    elif kleur == 'brown': kleur = 'bruine'
    gewicht = i['weight'] / 1000
    print(f'De "{naam}" ({lengte} letters) heeft een {kleur} kleur en een gewicht van {gewicht} kg.')