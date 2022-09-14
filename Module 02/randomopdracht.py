#leeftijd = input('Wat is jouw leeftijd?: ')
#nieuwe_leeftijd = int(leeftijd) * 3
#print('Als je 3x zo oud zou zijn, was je {} jaar oud geweest!'.format(nieuwe_leeftijd))

tijd_uren = int(input('Hoelaat is het en wil je alleen de uren benoemen (08)?: '))
tijd_minuten = int(input('Bedankt! En wil je nu alleen de minuten benoemen (30)?: '))
uren = 23 - tijd_uren
minuten = 60 - tijd_minuten
print('Dan duurt het nog {} uur en {} minuten voordat de dag voorbij is.'.format(uren, minuten))