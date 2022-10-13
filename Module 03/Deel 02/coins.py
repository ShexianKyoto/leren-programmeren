# name of student: 
# number of student:
# purpose of program: 
# function of program:
# structure of program: 

toPay = int(float(input('Amount to pay: '))* 100) # bedrag dat betaald moet worden (omgerekend naar cent)
paid = int(float(input('Paid amount: ')) * 100) # bedrag dat word betaald (omgerekend naar cent)
change = paid - toPay # berekent wisselgeld

if change > 0: # als er wisselgeld is
  coinValue = 500 # dan is muntwaarde 50 cent

  while change > 0 and coinValue > 0: # terwijl wisselgeld en muntwaarde hoger is dan 0
    nrCoins = change // coinValue # wisselgeld : muntwaarde (en afgerond)

    if nrCoins > 0: # als hoeveelheid munten hoger is dan 0
      print('return maximal', nrCoins, ' coins of ', coinValue, 'cents!') # print hoeveel munten met welke muntwaarde moet worden teruggegeven
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) # voer in hoeveel munten je terug hebt gegeven met de aangegeven muntstuk
      change -= nrCoinsReturned * coinValue # wisselgeld -= gegeven wisselgeld * waarde

# comment on code below: geeft aan 
    if coinValue == 500:
      coinValue = 300
    elif coinValue == 300:
      coinValue = 200
    elif coinValue == 200:
      coinValue = 50
    elif coinValue == 50:
      coinValue = 20
    elif coinValue == 20:
      coinValue = 10
    elif coinValue == 10:
      coinValue = 5
    elif coinValue == 5:
      coinValue = 2
    elif coinValue == 2:
      coinValue = 1
    else:
      coinValue = 0

if change > 0: # als wisselgeld hoger is dan nul, print al het geld dat niet terug gegeven is
  print('Change not returned: ', str(change) + ' cents')
else:
  print('done')