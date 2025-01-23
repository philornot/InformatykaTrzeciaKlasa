from interfejs import czytaj_plik

liczby = czytaj_plik(czy_przyklad=False, zwroc_int=False)


def zwroc_cyfry(liczba):
    lista_cyfr = []
    for i in liczba:
        lista_cyfr.append(i)

    return lista_cyfr

def stworz_najwieksza(liczba):
    cyfry = zwroc_cyfry(liczba)
    nowa_maks_liczba = ''
    for i in range(len(liczba)):
        maks_cyfra = max(cyfry)
        nowa_maks_liczba += maks_cyfra
        cyfry.remove(maks_cyfra)

    return int(nowa_maks_liczba)

def stworz_najmniejsza(liczba):
    cyfry = zwroc_cyfry(liczba)
    nowa_min_liczba = ''
    for i in range(len(liczba)):
        min_cyfra = min(cyfry)
        nowa_min_liczba += min_cyfra
        cyfry.remove(min_cyfra)

    return int(nowa_min_liczba)

mniejsza_licznik = 0
rowne_licznik = 0
wieksza_licznik = 0

for liczba in liczby:
    najmniejsza = stworz_najmniejsza(liczba)
    najwieksza = stworz_najwieksza(liczba)
    roznica = najwieksza-najmniejsza
    liczba = int(liczba)
    if roznica > liczba:
        wieksza_licznik += 1
    elif roznica == liczba:
        rowne_licznik += 1
    else:
        mniejsza_licznik += 1

print(f'Mniejsze: {mniejsza_licznik}\n'
      f'Równe: {rowne_licznik}\n'
      f'Większe: {wieksza_licznik}')
