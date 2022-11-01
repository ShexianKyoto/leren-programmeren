gastheer=input('Voer de naam van de gastheer in: ').lower()
gasten=13
drank=True
chips=True

if drank and gastheer != 'rudi' and gasten >= 5 and (gastheer != '' and gasten+1 <= 13):
    print('Start the party')
else:
    print('No party')