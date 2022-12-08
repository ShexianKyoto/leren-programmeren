# 32 landen, 8 groepen, per groep 1 land tegen ieder ander land, per groep 6 wedstrijden, vervolgens afvalrace
#vraag 1
land1, land2, land3 = input('Welke landen spelen in Groep A? (Alle landen op 1 zin):  ').split()

#vraag 2
w1 = dict(dL1 = input('Land1 Doelpunten:  '), dL2 = input('Land2 Doelpunten:  '), winnaar = '')
if w1['dL1'] > w1['dL2']: 
    w1['winnaar'] = land1
    w1['pL1'] = 3
else:
    w1['winnaar'] = land2
    w1['pL2'] = 3

w2 = dict(dL2 = input('Land2 Doelpunten:  '), dL3 = input('Land3 Doelpunten:  '), winnaar = '')
if w2['dL2'] > w2['dL3']: 
    w2['winnaar'] = land2
    w2['pL1'] = 3
else: 
    w2['winnaar'] = land3
    w2['pL2'] = 3

w3 = dict(dL1 = input('Land1 Doelpunten:  '), dL3 = input('Land3 Doelpunten:  '), winnaar = '')
if w3['dL1'] > w3['dL3']: 
    w3['winnaar'] = land1
    w3['pL1'] = 3
else: 
    w3['winnaar'] = land3
    w3['pL2'] = 3