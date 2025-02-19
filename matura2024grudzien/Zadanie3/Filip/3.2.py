from interfejs import czy_pierwsza, czytaj_plik

liczby = czytaj_plik(czy_przyklad=False)
licznik = {}
for liczba in liczby:
    licznik[liczba] = 0
    for i in range(2, liczba):
        if czy_pierwsza(i):
            if liczba % i == 0:
                licznik[liczba] += 1

licznik_liczby = 0
liczby_odp = []
for liczba in licznik:
    if licznik[liczba] == 5:
        licznik_liczby += 1
        liczby_odp.append(liczba)

print(liczby_odp, len(liczby_odp))
