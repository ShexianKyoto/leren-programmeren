koop_iphone = False
koop_iphone_50 = False
koop_samsung = False
gelijke_prijs = False
iphone_prijs = int(input('Hoe duur is de iPhone? (voer een getal in):  '))
samsung_prijs = int(input('Hoe duur is de Samsung? (voer een getal in):  '))
verschil_iphone = iphone_prijs - samsung_prijs
verschil_samsung = samsung_prijs - iphone_prijs

if iphone_prijs > samsung_prijs:
    print(f'De iPhone is het duurst, de telefoon kost: {iphone_prijs} Euro')
    print(f'De Samsung is het goedkoopst, de telefoon kost: {samsung_prijs} Euro')
elif samsung_prijs > iphone_prijs:
    print(f'De Samsung is het duurst, de telefoon kost: {samsung_prijs} Euro')
    print(f'De iPhone is het goedkoopst, de telefoon kost: {iphone_prijs} Euro')
else: print('Beide telefoons zijn even duur!')

if verschil_samsung <= 50:
    koop_iphone_50 = True
elif iphone_prijs > samsung_prijs:
    koop_iphone = True
    if koop_iphone_50 == True:
        koop_iphone = False
elif iphone_prijs < samsung_prijs:
    koop_samsung = True

if koop_iphone_50 == True:
    print(f'Het advies is dus de iPhone: {iphone_prijs},- te kopen. Deze is namelijk maar {verschil_samsung} euro duurder dan de Samsung: {samsung_prijs},-  !')
elif koop_samsung == True:
    print(f'Het advies is dus de Samsung te kopen. Deze is namelijk {verschil_samsung} Euro goedkoper dan de iPhone')
elif koop_iphone == True:
    print(f'Het advies is dus de iPhone te kopen. Deze is namelijk {verschil_iphone} Euro goedkoper dan de Samsung')