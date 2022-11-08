import random
userinput = None
geraden = 0

for round in range(0,20):
    round+=1
    guess = random.randint(1,1000)

    userinput = input('''Wil je een ronde starten?  [ Ja / Nee ]
''').lower()
    if userinput == 'ja':
        print(f'''
RONDE {round}''')
    else: break

    for attempt in range(0,10):
        attempt+=1
        print(f'POGING {attempt}')
        userinput = input('Voer een getal in: ').lower()
        if userinput == 'stop':
            print(f'''Jammer!
Bedankt voor het spelen :)
Aantal geraden: {geraden}
''')
            break
        elif userinput != 'stop':
            userinput = int(userinput)

        if userinput == guess:
            geraden+=1
            print(f'''GERADEN!
Aantal geraden: {geraden}
''')
            break

        elif userinput > guess:
            print('LAGER!')
            if userinput >= guess-20 and userinput <= guess+20: 
                print('Heel Warm!')
            elif userinput >= guess-50 and userinput <= guess+50:
                print('Warm!')

        elif userinput < guess:
            print('HOGER!')
            if userinput <= guess+20 and userinput >= guess-20: 
                print('Heel Warm!')
            elif userinput <= guess+50 and userinput >= guess-50: 
                print('Warm!')
        print('''
''')