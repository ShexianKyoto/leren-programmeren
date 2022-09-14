antwoord = input('Is de kaas geel? :').lower()
if antwoord == 'ja':
    antwoord1 = input('Zitten er gaten in? :').lower()
    if antwoord1 == 'ja':
        antwoord2 = input('Is de kaas belachelijk duur? :').lower()
        if antwoord2 == 'ja': 
            print('Het antwoord is Emmenthaler!')
        elif antwoord2 == 'nee':
            print('Het antwoord is Leerdammer!')        
    elif antwoord1 == 'nee':
        antwoord3 = input('Is de kaas hard als steen? :').lower()
        if antwoord3 == 'ja':
            print('Het antwoord is Parmigiano Reggiano!')
        elif antwoord3 == 'nee':
            print('Het antwoord is Goudse Kaas!')
if antwoord == 'nee':
    antwoord4 = input('Heeft de kaas blauwe schimmel? :').lower()
    if antwoord4 == 'ja':
        antwoord5 = input('Heeft de kaas een korst? :').lower()
        if antwoord5 == 'ja':
            print('Het antwoord is Blue de Rochbaron!')
        elif antwoord5 == 'nee':
            print('Het antwoord is Foume d\'Ambert!')
    elif antwoord4 == 'nee':
        antwoord6 = input('Heeft de kaas een stinkende geur? :').lower() #ik heb zelf een vraag verzonnen aangezien in het pdf 2x "heeft de kaas een korst?" stond
        if antwoord6 == 'ja':
            print('Het antwoord is Camembert!')
        elif antwoord6 == 'nee':
            print('Het antwoord is Mozzarella!')