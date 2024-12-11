from interfejs import odczytaj_czasy_przejazdu

# w bit18.txt jest "<km autostrady> <prędkość ciężarówek>"
# jeśli szybszy pojazd napotka wolniejszy, to zwalnia i dostosowuje prędkość do auta wolniejszego
# czyli jeśli na następnym km jest mniejsza v, tworzy się kolumna

def znajdz_kolumny(czy_przyklad=True):
    czasy = odczytaj_czasy_przejazdu(czy_przyklad)
    n = len(czasy)
    uzyte = [False] * n
    liczba_kolumn = 0

    for i in range(n):
        if not uzyte[i]:
            uzyte[i] = True
            liczba_kolumn += 1

            for j in range(i + 1, n):
                if not uzyte[j]:
                    roznica = czasy[i] - czasy[j]
                    if roznica < 0:
                        roznica = -roznica
                    if roznica < 0.000001:
                        uzyte[j] = True

    return liczba_kolumn


# Wywołanie funkcji
wynik = znajdz_kolumny(czy_przyklad=False)
print(wynik)