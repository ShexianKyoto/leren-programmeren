naam = input('Voer uw naam in: ')
leeftijd = input(f'Hallo {naam}, voer uw leeftijd in: ')
woonplaats = input(f'U bent {leeftijd} jaar oud, voer uw woonplaats in: ')
print(f'Ik heb uw gegevens voor u genoteerd: {naam}, {leeftijd}, {woonplaats}')
kloptGegevens = input('Kloppen de ingevoerde gegevens? ')
if kloptGegevens == 'Ja':
    print('Bedankt voor de informatie!')
elif kloptGegevens == 'Nee':
    naam = input('Voer uw naam in: ')
    leeftijd = input(f'Hallo {naam}, voer uw leeftijd in: ')
    woonplaats = input(f'U bent {leeftijd} jaar oud, voer uw woonplaats in: ')
    print(f'Ik heb de volgende gegevens voor u genoteerd: {naam}, {leeftijd}, {woonplaats}')
    kloptGegevens = input('Kloppen de ingevoerde gegevens? ')
else:
    print('Ik heb uw antwoord niet begrepen..')