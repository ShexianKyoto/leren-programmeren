#Rayen ter Wal | Pizza Calculator
print("Welkom!")
afmeting = input('Kies uw afmeting pizza (Small, Medium of Large): ')
print('-' * 30)

if afmeting == 'small':
    aantalsmall = int(input("Voer uw aantal Small pizza's in: "))
    print('-' * 30)
    prijssmall = 7.49
    kostensmall = aantalsmall * prijssmall
    print(f"{aantalsmall}   Small pizza's       €{kostensmall}")
    print('-' * 30)
    print("Bedankt voor het bestellen!")

elif afmeting == 'medium':
    aantalmedium = int(input("Voer uw aantal Medium pizza's in: "))
    print('-' * 30)
    prijsmedium = 8.99
    kostenmedium = aantalmedium * prijsmedium
    print(f"{aantalmedium}   Medium pizza's       €{kostenmedium}")
    print('-' * 30)
    print("Bedankt voor het bestellen!")

elif afmeting == 'large':
    aantallarge = int(input("Voer uw aantal Large pizza's in: "))
    print('-' * 30)
    prijslarge = 12.49
    kostenlarge = aantallarge * prijslarge
    print(f"{aantallarge}   Large pizza's       €{kostenlarge}")
    print('-' * 30)
    print("Bedankt voor het bestellen!")

else:
    print('Ik heb uw antwoord niet begrepen, probeer het opnieuw (zonder hoofdletters).')