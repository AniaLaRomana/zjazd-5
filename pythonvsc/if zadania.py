#Stwórz instrukcję, która będzie zwracała informację czy liczba jest parzysta czy też nieparzysta

liczba = 1 
if liczba % 2 == 0:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")

#Stwórz instrukcję, która porówna do siebie dwie zmienne posiadające wartości liczbowe -wskaże czy liczba jest równa, mniejsza czy większa od drugiej
liczba1 = 5
liczba2 = 3

if liczba1 == liczba2:
    print("Liczby sa takie same")
elif liczba1 > liczba2:
    print("Liczba1 jest wieksza niz liczba2")
else:
    print("Liczba1 jest mniejsza od liczby2")

#lub

def porownanie(liczba1, liczba2):
    if liczba1 == liczba2:
    print("Liczby sa takie same")
    elif liczba1 > liczba2:
    print("Liczba1 jest wieksza niz liczba2")
    else:
    print("Liczba1 jest mniejsza od liczby2")

liczba1 = 4
liczba2 = 5
porownanie(liczba1,liczba2)

