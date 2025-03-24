from interfejs import czytaj_plik

liczby = czytaj_plik()

licznik = 0
for liczba in liczby:
    if liczba[-1] == '2' and liczba[-2] == '0':
        print(liczba)
        licznik += 1

print(f'\nOdpowiedź: {licznik}')