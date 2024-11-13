# noinspection PyUnresolvedReferences
from interfejs import rozklad_na_czynniki, czytaj_plik, liczby_txt, przyklad_txt

# liczby = czytaj_plik(plik=przyklad_txt)
liczby = czytaj_plik(plik=liczby_txt)

maks_rozklad = 0
maks_liczba = 0

maks_unikalne = 0
maks_unikalne_liczba = 0
for liczba in liczby:
    rozklad = rozklad_na_czynniki(liczba)

    if len(rozklad) > maks_rozklad:
        maks_rozklad = len(rozklad)
        maks_liczba = liczba

    unikalne = []
    for element in rozklad:
        if element not in unikalne:
            unikalne.append(element)

    licznik = 0
    for i in unikalne:
        licznik += 1

    if len(unikalne) > maks_unikalne:
        maks_unikalne = len(unikalne)
        maks_unikalne_liczba = liczba

print(f'maks_liczba = {maks_liczba}\n'
      f'maks_rozklad = {maks_rozklad}\n\n'
      f'maks_unikalne_liczba = {maks_unikalne_liczba}\n'
      f'maks_unikalne = {maks_unikalne}')

print(f'\nOdpowiedź: {maks_liczba} {maks_rozklad} {maks_unikalne_liczba} {maks_unikalne}')
