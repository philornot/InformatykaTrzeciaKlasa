def czytaj_instrukcje(czy_przyklad=False):
    if czy_przyklad:
        plik = '../../dane2021maj/przyklad.txt'
    else:
        plik = '../../dane2021maj/przyklad.txt'

    with open(plik, 'r') as f:
        linie_pliku = f.readlines()

    instrukcje = []
    for linia_pliku in linie_pliku:
        instrukcja, litera = linia_pliku.split(' ')
        litera = litera.strip().lower()
        instrukcja_z_litera = instrukcja, litera
        instrukcje.append(instrukcja_z_litera)

    return instrukcje


def znajdz_indeks(litera, slowo):
    indeks = 0

    for i in slowo:
        if i == litera:
            return indeks
        indeks += 1



def dopisz(litera, obecne_slowo=''):
    return obecne_slowo + litera


def usun(obecne_slowo, ile_liter=1):
    return obecne_slowo[:-ile_liter]


def zmien(obecne_slowo, litera):
    return obecne_slowo.replace(obecne_slowo[-1], litera)


def przesun(obecne_slowo, litera):
    indeks = znajdz_indeks(litera, obecne_slowo)
    if indeks == -1:
        return obecne_slowo

    nowa_litera = chr((ord(litera) - ord('A') + 1) % 26 + ord('A')) if litera.isupper() else chr(
        (ord(litera) - ord('a') + 1) % 26 + ord('a'))

    return obecne_slowo[:indeks] + nowa_litera + obecne_slowo[indeks + 1:]
