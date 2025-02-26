def czytaj_plik(czy_przyklad=False):
    if czy_przyklad:
        plik = '../../dane2024czerwiec/slowa_przyklad.txt'
    else:
        plik = '../../dane2024czerwiec/slowa.txt'

    with open(plik, "r") as f:
        slowa = f.read()

    slowa = slowa.splitlines()

    lista_slow = []
    for slowo in slowa:
        lista_slow.append(slowo)