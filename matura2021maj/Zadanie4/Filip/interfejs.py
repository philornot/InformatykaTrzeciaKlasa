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



def dopisz(litera, obecne_slowo=''):
    return obecne_slowo + litera

def usun(ile_liter, obecne_slowo):
    return obecne_slowo[:-ile_liter]

print(usun(2, '12345'))