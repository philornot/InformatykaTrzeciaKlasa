from interfejs import czytaj_plik

dane = czytaj_plik()
licznik = 0
for i in dane:
    if i[-1] == '8':
        print(i)
        licznik += 1
print(f'\nOdpowiedź: {licznik} liczby')