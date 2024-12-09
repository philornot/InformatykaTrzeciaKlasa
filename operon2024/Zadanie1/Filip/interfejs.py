from jaraco.functools import retry


def odczytaj_dane(czy_przyklad=False):
    if czy_przyklad:
        plik = "przyklad11.txt"
    else:
        plik = "../../DaneOP/bit18.txt"

    with open(plik, "r", encoding="utf-8") as f:
        dane = f.readlines()

    dane_clean = []
    for dana in dane:
        dana = dana.strip('\n')
        dane_clean.append(dana)
    return dane_clean

def odczytaj_tabele(czy_przyklad=False):
    dane = odczytaj_dane(czy_przyklad=czy_przyklad)
    autostrada = {}
    for linijka in dane:
        km, predkosc = linijka.split(' ')
        autostrada[int(km)] = int(predkosc)
    return autostrada
