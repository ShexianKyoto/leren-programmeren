hoogte = float(input('Voer de de hoogte van het zwembad in (in meters(vb. 13.25)): '))
breedte = float(input('Voer de de breedte van het zwembad in (in meters(vb. 7.49)): '))
diepte = float(input('Voer de de diepte van het zwembad in (in meters(vb. 2.13)): '))
afstand = float(input('Voer de afstand in van ons bedrijf in aantal km: '))
kleur = str(input('Wat voor kleur afwering wilt u? ')).lower()

hoeveelM2 = hoogte*breedte
hoeveelM3 = hoeveelM2*diepte
print(hoeveelM3)
kostenUitgraven = hoeveelM3*25 #vaste prijs per m3
kostenAfvoeren = hoeveelM3*32.50 #vaste prijs per m

if afstand < 50 and hoeveelM3 < 20:
    kostenVoorrij = 100+(afstand*1.25)
elif afstand >= 50 and hoeveelM3 < 20:
    kostenVoorrij = 100+(afstand*1.15)
elif afstand < 50 and hoeveelM3 > 20:
    kostenVoorrij = 250+(afstand*2.15)
elif afstand >= 50 and hoeveelM3 > 20:
    kostenVoorrij = 250+(afstand*2.05)

if hoeveelM3 < 20 and kleur == 'rood':
    kostenAfwerken = 275*hoeveelM2
elif hoeveelM3 >= 20 and kleur == 'rood':
    kostenAfwerken = 220*hoeveelM2
elif hoeveelM3 < 20 and kleur != 'rood':
    kostenAfwerken = 100+(250*hoeveelM2)
elif hoeveelM3 >= 20 and kleur != 'rood':
    kostenAfwerken = 125+(200*hoeveelM2)

print(f'''Offerte voor een zwembad van 8 bij 3 bij 1,5 meter (inhoud: {hoeveelM3} m3)
Uitgraven                 :  €{kostenUitgraven}
Afvoeren Grond            :  €{kostenAfvoeren}
Voorrijkosten             :  €{kostenVoorrij}
Beton + tegel {hoeveelM2}m2      :  €{kostenAfwerken}
Totaal                    :  €{kostenUitgraven+kostenAfvoeren+kostenVoorrij+kostenAfwerken}
''')