#Rayen ter Wal | Exceptional Pizza Calculator
prijssmall = 7.49
prijsmedium = 8.99
prijslarge = 12.49
aantalpizza = 0
kosten = 0

print("Welkom!")
print('-' * 30)
while True:
    try: 
        afmeting = input('Kies uw afmeting pizza (Small, Medium of Large): ').lower()
        if afmeting in ('small','medium','large'):
            print('-' * 30)
            break
        else:  
            print('Oops! Voer 1 van de 3 aangegeven afmetingen in. ')
            continue 
    except: 
        print('Er is een fout opgetreden! Probeer het opnieuw.')  
        continue 

while True:
    aantalpizza = input(f'Voer uw aantal {afmeting} pizza\'s in: ')
    if aantalpizza.isnumeric(): break
    else:
        print(f'Oops! Voer uw AANTAL {afmeting} pizza(\'s) in!')
        continue


if afmeting == 'small':
    kosten = int(aantalpizza) * prijssmall
elif afmeting == 'medium':
    kosten = int(aantalpizza) * prijsmedium
elif afmeting == 'large': 
    kosten = int(aantalpizza) * prijslarge

print('-' * 30)
print(f"{aantalpizza}   {afmeting} pizza's       €{kosten}")
print('-' * 30)
print("Bedankt voor het bestellen.")