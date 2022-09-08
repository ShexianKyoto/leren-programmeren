personen = int(4)
ticketprijs = float(7.45)
entreekosten = personen * ticketprijs
gameseatprijs = float(0.37) #per 5 minuten
gameseatduur = int(5) 
gameseatprijsduur = int(45) #minuten
gameseat = gameseatprijsduur / gameseatduur * gameseatprijs

print('Prijs entree: ', entreekosten)
print('Prijs gameseat: ', gameseat)
print('Totaalprijs: ', entreekosten + gameseat)
