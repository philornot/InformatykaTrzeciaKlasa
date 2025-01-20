from interfejs import czy_pierwsza, czytaj_plik

liczby = czytaj_plik(czy_przyklad=True)
licznik = 0
for liczba in liczby:
    for i in range(3, liczba):
        if czy_pierwsza(i):
            if liczba % i == 0:
                licznik += 1
                print(liczba, i)

print(licznik)