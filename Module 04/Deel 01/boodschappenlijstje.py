lijstje = {}

fItem = input('(Naam) Voeg een item toe:   ')
fAmount = int(input(f'(Getal) Hoeveel stuks van {fItem}:    '))
lijstje.setdefault(fItem, fAmount)
nItem = ''

while nItem != 'nee':
    nItem = input('(Ja/Nee) Wil je een item toevoegen:   ').lower()
    if nItem == 'ja': 
        iName = input('(Naam) Wat voor item wilt u toevoegen:  ')
        iAmount = int(input(f'(Getal) Hoeveel stuks van {iName}:    '))
        lijstje.setdefault(iName, iAmount)
    elif nItem == 'nee':
        print('''
-=[ Boodschappenlijstje ]=-
''')
        for key in lijstje.keys():
            value = lijstje.get(key)
            print(f'''{value}x {key}

---------------------------
''')