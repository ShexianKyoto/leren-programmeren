#Rayen ter Wal | Exceptional Pizza Calculator

try:
    print("Welkom!")
    afmeting = input('Kies uw afmeting pizza (Small, Medium of Large): ').lower()
    print('-' * 30)
except:
    print('Er is een probleem opgelopen! Probeer het opnieuw of later nog eens.')

if afmeting == 'small':
    prijssmall = 7.49
    try:
        aantalsmall = int(input("Voer uw aantal pizza's in: "))
        kostensmall = aantalsmall * prijssmall
        print('-' * 30)
        print(f"{aantalsmall}   Small pizza's       €{kostensmall}")
        print('-' * 30)
        print("Bedankt voor het bestellen!")
    except:
        print('Er is een probleem opgelopen! Probeer het opnieuw of later nog eens.')

elif afmeting == 'medium':
    prijsmedium = 8.99
    try:
        aantalmedium = int(input("Voer uw aantal pizza's in: "))
        kostenmedium = aantalmedium * prijsmedium
        print('-' * 30)
        print(f"{aantalmedium}   Medium pizza's       €{kostenmedium}")
        print('-' * 30)
        print("Bedankt voor het bestellen!")
    except:
        print('Er is een probleem opgelopen! Probeer het opnieuw of later nog eens.')

elif afmeting == 'large':
    prijslarge = 12.49
    try:
        aantallarge = int(input("Voer uw aantal pizza's in: "))
        kostenlarge = aantallarge * prijslarge
        print('-' * 30)
        print(f"{aantallarge}   Large pizza's       €{kostenlarge}")
        print('-' * 30)
        print("Bedankt voor het bestellen!")
    except:
        print('Er is een probleem opgelopen! Probeer het opnieuw of later nog eens.')

else:
    print('Er is een probleem opgelopen! Probeer het opnieuw of later nog eens.')