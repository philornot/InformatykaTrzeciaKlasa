from interfejs import czytaj_plik

punkty = czytaj_plik()

def czy_pierwsza(liczba):
    if liczba < 2:
        return False
    i = 2
    while i**2 <= liczba:
        if liczba % i == 0:
            return False
        i += 1
    return True

znalezione = []
for p in punkty:
    liczba1, liczba2 = p
    if czy_pierwsza(liczba1) and czy_pierwsza(liczba2):
        znalezione.append(p)

print(len(znalezione))