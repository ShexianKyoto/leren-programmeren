aantalcroissant = input('Voer het aantal croissantjes in: ')
aantalcroissant1 = int(aantalcroissant)
croissantsp = 39 #cent
totaalcroissant = aantalcroissant1 * croissantsp

aantalstokbrood = input('Voer het aantal stokbroden in: ')
aantalstokbrood1 = int(aantalstokbrood)
stokbroodsp = 278 #cent
totaalstokbrood = aantalstokbrood1 * stokbroodsp

aantalkortingsbon = input('Voer het aantal kortingsbonnen in: ')
aantalkortingsbon1 = int(aantalkortingsbon)
kortingswaarde = 50 #cent

korting = aantalkortingsbon1 * kortingswaarde
totaalprijs = totaalcroissant + totaalstokbrood - korting

print(f'De feestlunch kost je bij de bakker {totaalprijs} eurocent voor de {aantalcroissant1} croissantjes en de {aantalstokbrood1} \
stokbroden als de {aantalkortingsbon1} kortingsbonnen nog geldig zijn!')