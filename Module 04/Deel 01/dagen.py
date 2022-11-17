werkdagen = ('maandag', 'dinsdag', 'woensdag', 'donderdag', 'vrijdag')
weekenddagen = ('zaterdag', 'zondag')
weekdagen = werkdagen + weekenddagen

print(f'Alle dagen van de week zijn: {weekdagen}')
print(f'De werkdagen zijn: {werkdagen}')
print(f'De weekenddagen zijn: {weekenddagen}')

print(f'Alle dagen van de week in omgekeerde volgorde zijn:')
for i in range(1, 8):
    print(f'{weekdagen[-i]}')
print(f'De werkdagen in omgekeerde volgorde zijn:')
for i in range(1, 6):
    print(f'{werkdagen[-i]}')
print(f'De weekenddagen in omgekeerde volgorde zijn:')
for i in range(1, 3):
    print(f'{weekenddagen[-i]}')