#Rayen ter Wal | Pizza Calculator
print("Welkom bij Domino's!")
afmeting = input('Kies uw afmeting pizza (Small, Medium of Large): ')
print('-' * 30)

if afmeting == 'small':
    aantalsmall = int(input("Voer uw aantal Small pizza's in: "))
    prijssmall = 7.49
    kostensmall = aantalsmall * prijssmall
    print(f"Totaalprijs voor {aantalsmall} Small pizza's is {kostensmall} euro.")
    print('-' * 30)
    print("Bedankt voor het bestellen bij Domino's")

elif afmeting == 'medium':
    aantalmedium = int(input("Voer uw aantal Medium pizza's in: "))
    prijsmedium = 8.99
    kostenmedium = aantalmedium * prijsmedium
    print(f"Totaalprijs voor {aantalmedium} Medium pizza's is {kostenmedium} euro.")
    print('-' * 30)
    print("Bedankt voor het bestellen bij Domino's")

elif afmeting == 'large':
    aantallarge = int(input("Voer uw aantal Large pizza's in: "))
    prijslarge = 12.49
    kostenlarge = aantallarge * prijslarge
    print(f"Totaalprijs voor {aantallarge} Large pizza's is {kostenlarge} euro.")
    print('-' * 30)
    print("Bedankt voor het bestellen bij Domino's")

else:
    print('Ik heb uw antwoord niet begrepen, probeer het opnieuw (zonder hoofdletters).')