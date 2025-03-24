from interfejs import czytaj_plik

liczby = czytaj_plik()


def osemkowa_na_dziesietna(liczba_osemkowa):
    liczba_dziesietna = 0
    potega = 0

    tekst_osemkowy = str(liczba_osemkowa)

    for cyfra in reversed(tekst_osemkowy):
        liczba_dziesietna += int(cyfra) * (8 ** potega)
        potega += 1

    return liczba_dziesietna

suma = 0
for liczba in liczby:
    if liczba[-1] == '8':
        print(f'{suma} + {liczba[:-1]} = {suma + osemkowa_na_dziesietna(liczba[:-1])}')
        suma += osemkowa_na_dziesietna(liczba[:-1])

print(f'\nOdpowiedź: {suma}')