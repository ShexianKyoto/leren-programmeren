iphone_prijs = int(input('Hoe duur is de iPhone? (voer een getal in):  '))
samsung_prijs = int(input('Hoe duur is de Samsung? (voer een getal in):  '))
zenfone_prijs = int(input('Hoe duur is de Zenfone? (voer een getal in):  '))
budget = 900

if budget < samsung_prijs and budget < iphone_prijs and budget < zenfone_prijs:
    print('Het advies is dus geen telefoon te kopen, ze zijn te duur.')
elif samsung_prijs == iphone_prijs == zenfone_prijs:
    print('Alle telefoons zijn even duur!')
elif zenfone_prijs - 100 < iphone_prijs and zenfone_prijs - 100 < samsung_prijs:
    print('Het advies is dus de ZenFone te kopen, deze is goedkoper dan de andere telefoons.')
elif iphone_prijs - samsung_prijs <= 50:
    print(f'De iPhone is het duurst, de telefoon kost: {iphone_prijs} Euro')
    print(f'De Samsung is het goedkoopst, de telefoon kost: {samsung_prijs} Euro')
    print(f'Het advies is dus de iPhone: {iphone_prijs},- te kopen. Deze is namelijk maar {iphone_prijs - samsung_prijs} euro duurder/goedkoper dan de Samsung: {samsung_prijs},-  !')
elif samsung_prijs < iphone_prijs + 50:
    print(f'De Samsung is het duurst, de telefoon kost: {samsung_prijs} Euro')
    print(f'De iPhone is het goedkoopst, de telefoon kost: {iphone_prijs} Euro')
    print(f'Het advies is dus de Samsung te kopen. Deze is namelijk {samsung_prijs - iphone_prijs} Euro duurder/goedkoper dan de iPhone')
elif zenfone_prijs - 100 < iphone_prijs and zenfone_prijs - 100 < samsung_prijs:
    print('')
