# Tuple - krotki rzydatne, gdy chcesz przechowywać kolekcję elementów,
# które nie powinny być modyfikowalne po utworzeniu. 
# Są również używane w wielu sytuacjach do zwracania wielu wartości z funkcji.

# Połączyć dwie krotki, tuple 
wig20 = ('CDR', 'PKO', 'PEO')
mwig40 = ('PLW', 'AMC', 'BFT')

print(wig20 + mwig40)

print('---')

# Zagnieźdź te obiekty w jedną krotkę
wig20 = ('CDR', 'PKO', 'PEO')
mwig40 = ('PLW', 'AMC', 'BFT')

all_objects = (wig20, mwig40)

print(all_objects)

print('---')

# Wstaw pomiędzy Kasię i Tomka krotkę ('Adam', 26)
adam = ('Adam', 26)
members = (('Kasia', 23), adam, ('Tomek', 19))
print(members)

print('---')

# liczbę wystąpień łańcucha znaków 'YES' w podanej krotce. 
default_settings = ('YES', 'NO', 'NO', 'YES', 'NO')
count_yes = [yes for yes in default_settings if yes == 'YES']
print(f"Number of occurrences of 'YES': {len(count_yes)}")

print('---')

# Posortuj tuple 
names = ('Monika', 'Tomek', 'Adam', 'Olaf')

print(sorted(names))

print('---')

# Sortowanie tupli + lambda + asc i desc

info = (('Monika', 19), ('Tomek', 21), ('Adam', 18), ('Jarek', 30))

ascending_sorted_info = sorted(info, key=lambda x: x[1], reverse=False)
descending_sorted_info = sorted(info, key=lambda x: x[1], reverse=True)

print(f"Ascending: {tuple(ascending_sorted_info)}")
print(f"Descending: {tuple(descending_sorted_info)}")

print('---')

# Wytnij trzyliterowy skrót dla spółki 'Playway' i wydrukuj do konsoli.
stocks = [
    ('Playway', ('PLW', 310)),
    ('CD Projekt', ('CDR', 300))
]

print(stocks[0][1][0])

print('---')

"""
Wykonaj poniższe operacje:
    połącz krotkę objectives1 z krotką coordinates1
    połącz krotkę objectives2 z krotką coordinates2
"""
objectives1 = ('Secure the perimeter', 'Neutralize enemy targets')
objectives2 = ('Provide medical assistance', 'Evacuate civilians')
    
coordinates1 = ((35.6895, 139.6917), (34.0537, -118.2424))
coordinates2 = ((40.7128, -74.0060), (51.5074, -0.1278))

firstMission = objectives1 + coordinates1
secondMission = objectives2 + coordinates2

print(f"First mission: {firstMission}")
print(f"Second mission: {secondMission}")


print('---')
# 
"""
Wykonaj poniższe kroki:
    wyznacz liczbę wszystkich stopni wojskowych - długość listy ranks - i przypisz do zmiennej num_ranks
    znajdź indeks krotki dla elementu 'Major' i przypisz do zmiennej major_index
    sprawdź, czy wartość 'Colonel' znajduje się w krotce ranks i przypisz do zmniennej colonel_present
"""
ranks = (
    'Private',
    'Corporal',
    'Sergeant',
    'Lieutenant',
    'Captain',
    'Major',
    'Colonel',
)

num_ranks = len(ranks)
major_index = ranks.index('Major')
colonel_present = [True if item == 'Colonel' else False for item in ranks ][6]

print(num_ranks)
print(major_index)
print(colonel_present)
