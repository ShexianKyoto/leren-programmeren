personen = int(input('Voer het aantal personen in: '))
ticketprijs = 745 #cent
entreekosten = personen * ticketprijs
gameseatprijs = 37 #cent per 5 minuten
gameseatduur = 5 #minuten
gameseatprijsduur = int(input('Voer uw gameseat duur in in minutes: '))
gameseat = gameseatprijsduur / gameseatduur * gameseatprijs
totaalprijs = entreekosten + gameseat 

print(f'Dit geweldige dagje-uit met {personen} mensen in de Speelhal met {gameseatprijsduur} minuten VR kost je maar \
{totaalprijs} eurocent.')