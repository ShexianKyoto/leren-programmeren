addition = 51
equasion = 50
iterate = 1
toPrint = "50",
while equasion <= 1000:
    equasion += addition
    toPrint += "+", addition
    print(f'{iterate}. {toPrint} = {equasion}')
    iterate += 1
    addition += 1