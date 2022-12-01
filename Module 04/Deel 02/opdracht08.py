from fruitmand import fruitmand

fruitmand.append({'name' : 'watermeloen','weight' : 3000,'color' : 'green','round' : False})
gewicht = 0
for i in fruitmand:
    gewicht += i['weight']
    print(gewicht)