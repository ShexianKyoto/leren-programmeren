import random

print('''
Om dit te spel te kunnen spelen moet je een nummer invoeren die correspondeert aan een bepaalde keuze.

Het is vrijdag avond na een avondje stappen besluit je naar huis te gaan waar je plotseling wordt ontvoerd.
Je wordt wakker in een soort grot ver weg in Egypte, je hoort en voelt trillingen van geluiden die door de gangen heen echoën.

Als je om je heen kijkt zie je alleen duisternis, alles is pikkedonker. 
Je hoort enge stemmen jouw naam roepen en er verschijnt licht aan het einde van de gang, je besluit om op onderzoek te gaan. 
Je loopt door de gang en hoort de stemmen verheffen terwijl het licht feller wordt. 
Je komt aan in een kamer waar het licht oorsprongt, hier zie je een altaar waar een bord op staat: 'TOMBE VAN ANUBIS'...''')

#######################################################
DEAD = False
EquipmentRoom = False

def randomNumber():
    global NUMBER
    NUMBER = random.randrange(0, 2)
    return NUMBER

def choice():
    global keuze
    keuzes = [1, 2, 3]
    keuze = 0
    while True:
        try:
            keuze = int(input('Maak een keuze: '))
            if keuze not in keuzes: 
                print('''| Ik heb uw keuze niet begrepen!
| Voer een getal in tussen 1 en 3...''')
                continue
            else: break
        except: 
            print('''### Er is een fout opgetreden! ###
|''')
            continue
    return keuze

#######################################################

while DEAD == False:
    print('''
[1]  Je bevindt je in een hal, er verschijnt een gang ten Oosten.
[2]  In het midden van de hal staat een tafel met daarop papierwerk en een kistje..
[3]  Aan het einde van de hal is het pikkedonker, je kan niet zo goed zien wat er is...

Waar ga je naar toe ?
''')
    choice()
#######################################################
    if keuze == 1:
        print('''
Je loopt naar de gang ten Oosten, er verschijnt opeens een deur. Je probeert deze te openen maar geen geluk.
[1]  Probeer de deur open te breken.
[2]  Keer terug naar de hal.
[3]  Onderzoek de deur voor een aanwijzing.
''')
        choice()
        if keuze == 1:
            randomNumber()
            if NUMBER == 0:
                print('''
De deur is met moeite open gevlogen!
Plotseling verschijnen er 3 nieuwe gangen.

Welke kant ga je op ?

[1]  de gang ten Westen
[2]  de gang ten Noorden
[3]  de gang ten Oosten
''')
                choice()
                if keuze == 1: 
                    print('''
Wat gebeurt er!? Alles trilt, is het een aardbeving? 
Er luid een harde knal en plotseling verschijnt Thoth, de God der Wijsheid! 
Hij beveelt jou zijn raadsel op te lossen in ruil voor vrijheid..

De raadsel luidt als volgt:  Wie was de eerste koning (Pharaoh) van Egypte?
''')
                    antwoord = input('Antwoord:  ').lower()
                    if antwoord == 'narmer':
                        print('''
Correct en gefeliciteerd!

Je hebt het avontuur overwonnen en wordt magisch door Thoth de Tombe uitgeplaatst.

Bedankt voor het spelen!
''')
                        DEAD = True
                    else:
                        print('''
Thoth is razend! Het antwoord is fout!! 
Voor het verspillen van zijn tijd neemt hij jouw ziel...

JE BENT DOOD!
''')
                        DEAD = True
                elif keuze == 2: 
                    randomNumber()
                    if NUMBER == 0:
                        print('''
Je loopt de gang uit maar vindt niks..
Je keert terug naar het begin van de hal.
''')
                    elif NUMBER == 1:
                        EquipmentRoom = True
                        print('''
De kamer lijkt op een storage room!
Je vindt hier uitrusting zoals een pijl en boog, een aantal pijlen en wat kledingstukken.
Je keert terug naar het begin van de hal.
''')
                elif keuze == 3: 
                    print('''
Een enge stem roept je naam! 
Apep, de Vijand van Licht verschijnt voor je!

Wat doe je ?

[1]  Vecht Apep!
[2]  Probeer te vluchten!
''')
                    choice()
                    if keuze == 1:
                        if EquipmentRoom == True:
                            print('''
Je verslaat Apep met de gevonden uitrusting uit de storage room!
Je erft alle krachten van Apep, teleporteert uit de Tombe!

Gefeliciteerd en bedankt voor het spelen!
''')
                            DEAD = True
                        elif EquipmentRoom == False:
                            print('''
Zonder uitrusting maak je geen schijn van kans!
Apep verslaat jou!

JE BENT DOOD!
''')
                            DEAD = True
                    elif keuze == 2:
                        print('''
Vluchten was geen slim plan, Apep steekt zijn zwaard door jouw rug..
Je valt op de grond en bloed dood.

JE BENT DOOD!
''')
                        DEAD = True
            elif NUMBER == 1:
                print('''
De deur lijkt niet te openen.
Je keert terug naar het begin van de hal.
''')
        elif keuze == 2:
            print('''
Je keert terug naar het begin van de hal.
''')
        elif keuze == 3:
            print('''
De deur lijkt magisch gesloten te zijn, er is geen kans dat je deze open krijgt.
Je keert terug naar het begin van de hal.
''')
    elif keuze == 2:
        print('''
Je loopt naar de tafel in het midden van de hal, er ligt hier wat leeg papierwerk en een gesloten kistje.
Je keert terug naar het begin van de hal.
''')
    elif keuze == 3:
        print('''
Je loopt richting het einde van de hal..
Plotseling zie je een schaduw figuur, je stopt met lopen.

Welke kant ga je op ?

[1]  Loop door, je kent geen angst!
[2]  Keer terug naar het begin van de hal.
''')
        choice()
        if keuze == 1:
            print('''
Je loopt door en het schaduw figuur beweegt mee, plotseling verdwijnt het opeens...
Je voelt een rilling over je rug en kijkt uit schrik naar achter.
Ammit, de Verslinder van de Dood staat achter je.

[1]  Vecht Ammit!
[2]  Probeer te vluchten!
''')
            choice()
            if keuze == 1:
                if EquipmentRoom == True:
                    print('''
Je verslaat Ammit met de gevonden uitrusting uit de storage room!
Je erft alle krachten van Ammit en beweegt door de schaduwen om de Tombe te ontkomen!

Gefeliciteerd en bedankt voor het spelen!
''')
                    DEAD = True
                elif EquipmentRoom == False:
                    print('''
Zonder uitrusting maak je geen schijn van kans!
Ammit neemt jouw leven!

JE BENT DOOD!
''')
                    DEAD = True
            elif keuze == 2:
                print('''
Vluchten was geen slim plan, Ammit beweegt door de schaduwen en valt aan!..
Je valt op de grond en het hele lichaam verstijft vanwege zijn duistere krachten.

JE BENT DOOD!
''')
                DEAD = True
        elif keuze == 2:
            print('''
Je keert terug naar het begin van de hal.
''')