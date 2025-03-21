def czytaj_plik(czy_przyklad=False, zwroc_int=True):
    if czy_przyklad:
        plik = '../../dane2024grudzien/liczby_przyklad.txt'
    else:
        plik = '../../dane2024grudzien/liczby.txt'

    with open(plik, 'r', encoding='utf-8') as f:
        linie = f.readlines()

    linie_clean = []
    for linia in linie:
        linia = linia.strip()
        if zwroc_int:
            linie_clean.append(int(linia))
        else:
            linie_clean.append(linia)

    return linie_clean

def czy_pierwsza(liczba):
    if liczba < 2:
        return False
    i = 2

    while i * i <= liczba:
        if liczba % i == 0:
            return False
        i = i + 1

    return True