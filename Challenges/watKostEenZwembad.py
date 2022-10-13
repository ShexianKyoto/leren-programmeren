# Voorrijkosten (afhankelijk van de afstand en grootte van het zwembad)
#   inhoud zwembad mag afronden 2 decimalen, joris kijkt niet naar kruiwagen grond meer of minder.
# Kosten uitgraven (gerekend in m3(kubieke))
# Kosten afvoeren grond (gerekend per m3)
# Kosten aanbrengen wand en vloer (gerekend per m2(vierkante))
# Test uitzondering, commit en push na elke stap!

hoeveelGrond = (8*3)*1.5
print(hoeveelGrond)

kostenUitgraven = hoeveelGrond*25 #per m3
kostenAfvoeren = hoeveelGrond*32.50 #per m3
print(f'''Offerte voor een zwembad van 8 bij 3 bij 1,5 meter (inhoud: {hoeveelGrond} m3)
Uitgraven      :  €{kostenUitgraven}
Afvoeren Grond :  €{kostenAfvoeren}
Totaal         :  €{kostenUitgraven+kostenAfvoeren}
''')
