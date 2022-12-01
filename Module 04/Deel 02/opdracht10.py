from fruitmand import fruitmand

def sorteer(i):
    return i['weight']
fruitmand.sort(key=sorteer)
for i in fruitmand: print(i['name'], i['weight']/1000, 'kg')