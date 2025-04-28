def czytaj_dane(czy_przyklad=False):
    if czy_przyklad:
        plik = '../../dane2021czerwiec/przyklad.txt'
    else:
        plik = '../../dane2021czerwiec/napisy.txt'

    with open(plik, 'r') as f:
        dane = f.readlines()
    dane_clean = []
    for dana in dane:
        dana = dana.strip()
        dane_clean.append(dana)

    return dane_clean