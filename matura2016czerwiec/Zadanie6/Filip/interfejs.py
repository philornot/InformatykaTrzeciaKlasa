def czytaj_plik():
    plik = '../../dane2016czerwiec/liczby.txt'
    with open(plik, "r") as f:
        dane = f.read().splitlines()
    return dane

