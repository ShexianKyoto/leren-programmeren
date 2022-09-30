antwoord = None
iterate = 0
while antwoord != 'quit':
    antwoord = input('? ')
    print(f'Iteration: {iterate}')
    if antwoord != 'quit':
        iterate += 1
    if antwoord == 'quit':
        print('QUIT!')