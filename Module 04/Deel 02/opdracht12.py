from fruitmand import fruitmand

def sorteer(i):
    return len(i['name'])
fruitmand.sort(key=sorteer)

naam = fruitmand[-1]['name']
lengte = len(fruitmand[-1]['name'])
kleur = fruitmand[-1]['color']
if kleur == 'orange': kleur = 'oranje'
elif kleur == 'pink': kleur = 'roze'
gewicht = fruitmand[-1]['weight'] / 1000

print(f'De "{naam}" ({lengte} letters) heeft een {kleur} kleur en een gewicht van {gewicht} kg.')