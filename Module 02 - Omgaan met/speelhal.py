personen = int(4)
ticketprijs = float(7.45)
entreekosten = personen * ticketprijs
gameseatprijs = float(0.37) #per 5 minuten
gameseatduur = int(5) 
gameseatprijsduur = int(45) #minuten
gameseat = gameseatprijsduur / gameseatduur * gameseatprijs
totaalprijs = entreekosten + gameseat 

print('Prijs entree: ', entreekosten)
print('Prijs gameseat: ', gameseat)
print('Totaalprijs: ', totaalprijs)

print(f'Dit geweldige dagje-uit met {personen} mensen in de Speelhal met {gameseatprijsduur} minuten VR kost je maar \
{totaalprijs} euro.')