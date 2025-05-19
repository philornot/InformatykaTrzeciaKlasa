from interfejs import czytaj_dane, zapisz_wynik

napisy = czytaj_dane(czy_przyklad=False)

def palindrom(t):
    i = 0
    j = len(t) - 1
    while i < j:
        if t[i] != t[j]:
            return False
        i += 1
        j -= 1
    return True

for napis in napisy:
    napisy_pali.