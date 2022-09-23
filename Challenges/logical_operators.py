ScoreE = int(input('Voer uw score voor excellente acties in: '))
if ScoreE > 6 or ScoreE < 0:
    print('De score voor excellente acties mag niet hoger dan 6 of lager dan 0 zijn! Probeer het opnieuw.')
    ScoreE = int(input('Voer uw score voor excellente acties OPNIEUW in: '))

ScoreP = int(input('Voer uw score voor professionele acties in: '))
if ScoreP > 8 or ScoreP < 0:
    print('De score voor professionele acties mag niet hoger dan 8 of lager dan 0 zijn! Probeer het opnieuw.')
    ScoreP = int(input('Voer uw score voor professionele acties OPNIEUW in: '))

ScoreO = int(input('Voer uw score voor onprofessionele acties in: '))
if ScoreO > 5 or ScoreO < 0:
    print('De score voor onprofessionele acties mag niet hoger dan 5 of lager dan 0 zijn! Probeer het opnieuw.')
    ScoreO = int(input('Voer uw score voor onprofessionele acties OPNIEUW in: '))

ScoreS = int(input('Voer uw score voor slechte acties in: '))
if ScoreS > 2 or ScoreS < 0:
    print('De score voor slechte acties mag niet hoger dan 2 of lager dan 0 zijn! Probeer het opnieuw.')
    ScoreS = int(input('Voer uw score voor slechte acties OPNIEUW in: '))

scoreG = False
scoreV = False
scoreO = False

if ScoreP == 8 and ScoreE > 4 and ScoreO == 0 and ScoreS == 0:
    scoreG = True
elif ((ScoreP + ScoreE - ScoreO >= 8) and ScoreS == 0) or (ScoreS <= 1 and (ScoreP + ScoreE - ScoreO) > 9):
    scoreV = True
else: scoreO = True

print('Uw uitslag is berekend! ')
print(f'''Score Goed: {scoreG} 
Score Voldoende: {scoreV}
Score Onvoldoende: {scoreO}''')