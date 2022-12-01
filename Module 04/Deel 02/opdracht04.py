from fruitmand import fruitmand
import random

aantal = int(input('Voer een aantal in: '))
for i in range(aantal):
    x = random.randint(0, (len(fruitmand)-1))
    print(fruitmand[x]['name'])