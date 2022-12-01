from fruitmand import fruitmand

def sorteer(i):
    return len(i['name'])
fruitmand.sort(key=sorteer)

naam = fruitmand[-1]['name']
lengte = len(fruitmand[-1]['name'])
kleur = fruitmand[-1]['color']
if kleur == 'yellow': kleur = 'gele'
elif kleur == 'green': kleur = 'groene'
elif kleur == 'orange': kleur = 'oranje'
elif kleur == 'red': kleur = 'rode'
elif kleur == 'brown': kleur = 'bruine'
gewicht = fruitmand[-1]['weight'] / 1000

print(f'De "{naam}" ({lengte} letters) heeft een {kleur} kleur en een gewicht van {gewicht} kg.')