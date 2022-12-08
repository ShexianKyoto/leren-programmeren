# 32 landen, 8 groepen, per groep 1 land tegen ieder ander land, per groep 6 wedstrijden, vervolgens afvalrace
#vraag 1
land1, land2, land3 = input('Welke 3 landen spelen in Groep A?(Landen achter elkaar met spaties):  ').split()

#vraag 2
w1 = dict(dL1 = int(input(f'{land1} Wedstrijd 1 Doelpunten:  ')), pL1 = 0, dL2 = int(input(f'{land2} Wedstrijd 1 Doelpunten:  ')), pL2 = 0, winnaar = '')
if w1['dL1'] > w1['dL2']: 
    w1['winnaar'] = land1
    w1['pL1'] = 3
else:
    w1['winnaar'] = land2
    w1['pL2'] = 3

w2 = dict(dL2 = int(input(f'{land2} Wedstrijd 2 Doelpunten:  ')), pL2 = 0, dL3 = int(input(f'{land3} Wedstrijd 2 Doelpunten:  ')), pL3 = 0, winnaar = '')
if w2['dL2'] > w2['dL3']:
    w2['winnaar'] = land2
    w2['pL2'] = 3
else: 
    w2['winnaar'] = land3
    w2['pL3'] = 3

w3 = dict(dL1 = int(input(f'{land1} Wedstrijd 3 Doelpunten:  ')), pL1 = 0, dL3 = int(input(f'{land3} Wedstrijd 3 Doelpunten:  ')), pL3 = 0, winnaar = '')
if w3['dL1'] > w3['dL3']: 
    w3['winnaar'] = land1
    w3['pL1'] = 3
else: 
    w3['winnaar'] = land3
    w3['pL3'] = 3

scores = {
    'land1': {
    'dp': w1.get('dL1') + w3.get('dL1'),
    'pt': w1.get('pL1') + w3.get('pL1')
    },
    'land2': {
    'dp': w1.get('dL2') + w2.get('dL2'),
    'pt': w1.get('pL2') + w2.get('pL2')
    },
    'land3': {
    'dp': w2.get('dL3') + w3.get('dL3'),
    'pt': w2.get('pL3') + w3.get('pL3')
    }}

#vraag 3
print(f'''
Wedstrijd {land1} - {land2} eindigde in: {w1['dL1']} - {w1['dL2']}
Overzicht Groep A
{land1}: punten {scores['land1'].get('pt')}; doelsaldo {scores['land1'].get('dp')}
{land2}: punten {scores['land2'].get('pt')}; doelsaldo {scores['land2'].get('dp')}
{land3}: punten {scores['land3'].get('pt')}; doelsaldo {scores['land3'].get('dp')}
''')