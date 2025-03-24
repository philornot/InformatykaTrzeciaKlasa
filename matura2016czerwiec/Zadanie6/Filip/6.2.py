from interfejs import czytaj_plik

liczby = czytaj_plik()
licznik = 0

for liczba in liczby:
    if liczba[-1] == '4' and '0' not in liczba:
        print(liczba)
        licznik += 1

print(f'\nOdpowiedź: {licznik}')