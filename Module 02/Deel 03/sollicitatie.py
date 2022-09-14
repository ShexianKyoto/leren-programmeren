print('Om te solliciteren voor de vacature van \'Circusdirecteur voor Circus HotelDeBoer\' moet u voldoen aan bepaalde eisen,\
    hiervoor zullen wij u een paar vragen stellen. Als het blijkt dat u voldoet aan de benodigde criteria heeft u kans op\
    een uitnodiging van een sollicitatiegesprek.')

ervaring_dierendressuur = int(input('Hoeveel jaar praktijkervaring heeft u met dieren-dressuur?: '))
ervaring_jongleren = int(input('Hoeveel jaar ervaring heeft u met jongleren?: '))
ervaring_acrobatiek = int(input('Hoeveel jaar praktijkervaring heeft u met acrobatiek?: '))
bezit_diplomaMBO4 = input('Bent u in bezit van het Diploma MBO-4 ondernemen?: ').lower()
bezit_geldigVrachtwagenRijbewijs = input('Bent u in bezit van een geldig vrachtwagenrijbewijs?: ').lower()
bezit_hogeHoed = input('Bent u in bezit van een hoge hoed?: ').lower()
geslacht = input('Voer uw geslacht in: ').lower()
if geslacht == 'man':
    heeft_snor = input('Heeft u een snor?: ').lower()
    if heeft_snor == 'ja':
        snorlengte = input('Voer uw snorlengte in cm in: ').lower()
elif geslacht == 'vrouw':
    heeft_rood_krulhaar = input('Heeft u rood krulhaar?: ').lower()
    if heeft_rood_krulhaar == 'ja':
        lengte_krulhaar = input('Voer uw krulhaarlengte in cm in: ').lower()
lichaamslengte = input('Voer uw lichaamslengte in cm in: ').lower()
lichaamsgewicht = input('Voer uw gewicht in kg in: ').lower()
certificaat_overlevenMetGevaarlijkPersoneel = input('Bezit u over een certificaat \'Overleven met gevaarlijk personeel\'?: ').lower()
heeft_auto = input('Beschikt u over een auto met 500 pk?: ').lower()
heeft_fiets = input('Beschikt u over een elektrische fiets?: ').lower()
heeft_conditie = input('Beschikt u over een goede conditie i.v.m sportdag?: ').lower()
heeft_partner = input('Heeft u een partner?: ').lower()

toelating = False
if ervaring_dierendressuur >= 4 or ervaring_jongleren >= 5 or ervaring_acrobatiek >= 3: toelating = True
if bezit_diplomaMBO4 == 'ja': toelating = True
if bezit_geldigVrachtwagenRijbewijs == 'ja': toelating = True
if bezit_hogeHoed == 'ja': toelating = True
if geslacht == 'man' and heeft_snor == 'ja' and snorlengte >= 10: toelating = True
if geslacht == 'vrouw' and heeft_rood_krulhaar == 'ja' and lengte_krulhaar >= 20: toelating = True
if lichaamslengte >= 150: toelating = True
if lichaamsgewicht >= 90: toelating = True
if certificaat_overlevenMetGevaarlijkPersoneel == 'ja': toelating = True

if toelating == True: print('Gefeliciteerd! U maakt kans op een sollicitatiegesprek.')
elif toelating == False: print('Helaas! U maakt geen kans op een sollicitatiegesprek.')