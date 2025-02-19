def czytaj_plik(czy_przyklad=False):
    if czy_przyklad:
        plik = "../../dane2019maj/przyklad.txt"
    else:
        plik = "../../dane2019maj/liczby.txt"

    with open(plik) as f:
        linie = f.readlines()

    linie_clean = []
    for linia in linie:
        linia_clean = int(linia.strip())
        linie_clean.append(linia_clean)

    return linie_clean
