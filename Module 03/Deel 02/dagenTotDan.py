dagen = ['maandag','dinsdag','woensdag','donderdag','vrijdag','zaterdag','zondag']
dag = None
while dag not in dagen:
    dag = input('Voer uw dag in (volledig uitgeschreven): ')
    if dag in dagen:
        print(f'Gekozen dag: {dag}')
        if dag == 'maandag': print(dagen[1:7])
        elif dag == 'dinsdag': print(dagen[2:7], dagen[0:1])
        elif dag == 'woensdag': print(dagen[3:7], dagen[0:2])
        elif dag == 'donderdag': print(dagen[4:7], dagen[0:3])
        elif dag == 'vrijdag': print(dagen[5:7], dagen[0:4])
        elif dag == 'zaterdag': print(dagen[6:7], dagen[0:5])
        elif dag == 'zondag': print(dagen[0:6])
    else: print(f'Is {dag} een dag?')