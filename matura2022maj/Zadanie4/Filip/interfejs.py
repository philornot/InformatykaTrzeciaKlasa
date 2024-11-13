liczby_txt = '../../dane2022maj/liczby.txt'
przyklad_txt = '../../dane2022maj/przyklad.txt'


def czytaj_plik(plik=liczby_txt):
    linijki = []
    with open(plik, encoding='utf-8') as p:
        linijki_raw = p.readlines()
    for linijka in linijki_raw:
        linijki.append(int(linijka.strip()))

    return linijki
