from interfejs import czytaj_plik

liczby = czytaj_plik(czy_przyklad=True, zwroc_int=False)


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

print(liczby[0],stworz_najwieksza(liczby[0]))
print(liczby[0],stworz_najmniejsza(liczby[0]))

mniejsza_licznik = 0
wieksza_licznik = 0
rowne_licznik = 0
for liczba in liczby:
    najmniejsza = stworz_najmniejsza(liczba)
    najwieksza = stworz_najwieksza(liczba)
    if najwieksza - najmniejsza > 0:
        mniejsza_licznik += 1
    elif najwieksza - najmniejsza == 0:
        rowne_licznik += 1
    elif najwieksza - najmniejsza < 0:
        mniejsza_licznik += 1
    else:
        print(f'wtf: {najwieksza - najmniejsza}')