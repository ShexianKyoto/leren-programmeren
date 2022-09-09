a = int(input('Voer een geheel getal in: '))
b = int(input('Voer nog een geheel getal in: '))

if a > b:   #input en if-statement
    Max = a
    print('a is het grootste getal', Max)

elif a < b:     #elif-statement
    Min = a
    print('a is het kleinste getal', Min)

else:       #else-statement
    print('a en b zijn even groot')