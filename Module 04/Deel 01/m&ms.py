import random

kleuren = ('oranje', 'blauw', 'groen', 'bruin')
hoeveelheid = int(input('Hoeveel M&M\'s wil je toevoegen: '))
zak = []

for willekeurig in range(1, hoeveelheid+1):
    randomkleur = random.choice(kleuren)
    zak.append(randomkleur)
print(f'Je hebt {hoeveelheid} kleuren in de zak!')
print(zak)