aantalcroissant = int(17)
croissantsp = float(0.39)
totaalcroissant = aantalcroissant * croissantsp
aantalstokbrood = int(2)
stokbroodsp = float(2.78)
totaalstokbrood = aantalstokbrood * stokbroodsp
aantalkortingsbon = int(3)
kortingswaarde = float(0.50)
korting = aantalkortingsbon * kortingswaarde

print('Prijs Croissantjes: ', totaalcroissant)
print('Prijs Stokbroden: ', totaalstokbrood)
print('Korting: ', aantalkortingsbon * kortingswaarde)
print('Totaalprijs: ', totaalcroissant + totaalstokbrood - korting)