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
import random
aantal = int(input('Voer een aantal in: '))
for i in range(aantal):
    x = random.randint(0, (len(fruitmand)-1))
    print(fruitmand[x]['name'])