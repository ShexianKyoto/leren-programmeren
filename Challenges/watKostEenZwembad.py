# Voorrijkosten (afhankelijk van de afstand en grootte van het zwembad)
#   inhoud zwembad mag afronden 2 decimalen, joris kijkt niet naar kruiwagen grond meer of minder.
# Kosten uitgraven (gerekend in m3(kubieke))
# Kosten afvoeren grond (gerekend per m3)
# Kosten aanbrengen wand en vloer (gerekend per m2(vierkante))
# Test uitzondering, commit en push na elke stap!
hoogte = float(input('Voer de de hoogte van het zwembad in (in meters(vb. 13.25)): '))
breedte = float(input('Voer de de breedte van het zwembad in (in meters(vb. 7.49)): '))
diepte = float(input('Voer de de diepte van het zwembad in (in meters(vb. 2.13)): '))
hoeveelGrond = (hoogte*breedte)*diepte
print(hoeveelGrond)

kostenUitgraven = hoeveelGrond*25 #vaste prijs per m3
kostenAfvoeren = hoeveelGrond*32.50 #vaste prijs per m3
kostenVoorrij = 250+(60*2.05)

print(f'''Offerte voor een zwembad van 8 bij 3 bij 1,5 meter (inhoud: {hoeveelGrond} m3)
Uitgraven      :  €{kostenUitgraven}
Afvoeren Grond :  €{kostenAfvoeren}
Voorrijkosten  :  €{kostenVoorrij}
Totaal         :  €{kostenUitgraven+kostenAfvoeren+kostenVoorrij}
''')
