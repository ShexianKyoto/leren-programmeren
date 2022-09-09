a = int(input('Voer een geheel getal in: '))
b = int(input('Voer nog een geheel getal in: '))

if a > b:   #input en if-statement
    Max = a
    Min = b
    print('Het minimum is: ', Min)
    print('Het maximum is: ', Max)

elif a < b:     #elif-statement
    Min = a
    Max = b
    print('Het minimum is: ', Min)
    print('Het maximum is: ', Max)
    
else:       #else-statement
    print('a en b zijn even groot')