import random
userinput = None

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
            print('''Jammer!
Bedankt voor het spelen :)
''')
            break
        elif userinput != 'stop':
            userinput = int(userinput)

        if userinput == guess:
            print('''GERADEN!
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