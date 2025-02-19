def czytaj_plik(czy_przyklad=False):
    if czy_przyklad:
        plik = '../../dane2024grudzien/prostokaty_przyklad.txt'
    else:
        plik = '../../dane2024grudzien/prostokaty.txt'

    with open(plik, 'r', encoding='utf-8') as f:
        linie = f.readlines()

    linie_clean = []
    for linia in linie:
        linia = linia.strip()
        linie_clean.append(linia)

    return linie_clean


def odczytaj_wymiary(czy_przyklad=False):
    wymiary_lista = enumerate(czytaj_plik(czy_przyklad=czy_przyklad))
    wysokosc_tabela = {}
    szerokosc_tabela = {}
    for wymiar in wymiary_lista:
        i, wymiary = wymiar[0], wymiar[1]
        wysokosc, szerokosc = wymiary.split(' ')
        wysokosc_tabela[i] = int(wysokosc)
        szerokosc_tabela[i] = int(szerokosc)

    return wysokosc_tabela, szerokosc_tabela

# zwraca list z tuplami (wysokosc, szerokosc)
def odczytaj_prostokaty(czy_przyklad=False):
    prostokaty = []
    wysokosc_tabela, szerokosc_tabela = odczytaj_wymiary(czy_przyklad)
    for i in wysokosc_tabela:
        nowy_prostokat = wysokosc_tabela[i], szerokosc_tabela[i]
        prostokaty.append(nowy_prostokat)
    return prostokaty