def czytaj_liczby_z_pliku(czy_przyklad=False):
    if czy_przyklad:
        plik = "../../DANE/przyklad.txt"
    else:
        plik = "../../DANE/liczby.txt"

    with open(plik, "r", encoding="utf-8") as f:
        linie = f.readlines()

    linie_clean = []
    for linia in linie:
        linia = linia.replace('\n', '')
        linie_clean.append(int(linia))

    return linie_clean  # zwraca listę int-ów

def odbij_liczbe(liczba): # przyjmuje int
    liczba = str(liczba)
    liczba_reverse = ""
    i = len(liczba)
    for j in range(len(liczba)):
        liczba_reverse += liczba[i-1]
        i -= 1
    return int(liczba_reverse) # zwraca odwrócony int

def czy_podzielna_przez_17(liczba):
    if liczba % 17 != 0:
        return False
    else:
        return True
