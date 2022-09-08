aantalcroissant = int(17)
croissantsp = float(0.39)
totaalcroissant = aantalcroissant * croissantsp
aantalstokbrood = int(2)
stokbroodsp = float(2.78)
totaalstokbrood = aantalstokbrood * stokbroodsp
aantalkortingsbon = int(3)
kortingswaarde = float(0.50)
korting = aantalkortingsbon * kortingswaarde
totaalprijs = totaalcroissant + totaalstokbrood - korting

print('Prijs Croissantjes: ', totaalcroissant)
print('Prijs Stokbroden: ', totaalstokbrood)
print('Korting: ', aantalkortingsbon * kortingswaarde)
print('Totaalprijs: ', totaalprijs)

print(f'De feestlunch kost je bij de bakker {totaalprijs} euro voor de {aantalcroissant} croissantjes en de {aantalstokbrood} \
stokbroden als de {aantalkortingsbon} kortingsbonnen nog geldig zijn!')