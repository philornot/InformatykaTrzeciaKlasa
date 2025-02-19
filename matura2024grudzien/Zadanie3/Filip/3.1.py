from interfejs import czytaj_plik

liczby = czytaj_plik(czy_przyklad=False)
licznik = 0
pierwsza = 0
for liczba in liczby:
    pierwiastek = liczba ** 0.5
    if pierwiastek - int(pierwiastek) == 0:
        if licznik == 0:
            pierwsza = liczba
        licznik += 1

print(licznik, pierwsza)