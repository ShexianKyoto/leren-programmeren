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
kleuren = []
for i in fruitmand:
    if i['color'] not in kleuren: kleuren.append(i['color'])
print(kleuren)

userinput = ''
while userinput not in kleuren:
    userinput = input('Kies een van de gegeven kleuren: ')
    if userinput not in kleuren:
        print(f'De kleur {userinput} zit niet in de fruitmand!')

rond = 0
nrond = 0
for i in fruitmand:
    if i['round'] and userinput == i['color']: rond+=1
    elif not i['round'] and userinput == i['color']: nrond+=1

if rond > nrond: print(f'Er zijn {rond} meer ronde vruchten dan niet ronde vruchten in de kleur {userinput}.')
elif rond < nrond: print(f'Er zijn {rond} minder ronde vruchten dan niet ronde vruchten in de kleur {userinput}.')
else: print(f'Er zijn {rond} ronde vruchten en {nrond} niet ronde vruchten in de kleur {userinput}')