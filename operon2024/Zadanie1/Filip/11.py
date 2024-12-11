from interfejs import odczytaj_czasy_przejazdu

# w bit18.txt jest "<km autostrady> <prędkość ciężarówek>"
# jeśli szybszy pojazd napotka wolniejszy, to zwalnia i dostosowuje prędkość do auta wolniejszego
# czyli jeśli na następnym km jest mniejsza v, tworzy się kolumna

def znajdz_kolumny(czy_przyklad=True):
    pozycje, predkosci = odczytaj_pozycje_i_predkosci(czy_przyklad)
    n = len(pozycje)
    uzyte = [False] * n
    liczba_kolumn = 0

    for i in range(n):
        if not uzyte[i]:
            uzyte[i] = True
            liczba_kolumn += 1

            for j in range(i + 1, n):
                if not uzyte[j]:
                    # Jeśli pozycja/prędkość jest taka sama, to ciężarówki tworzą kolumnę
                    if pozycje[i] * predkosci[j] == pozycje[j] * predkosci[i]:
                        uzyte[j] = True

    return liczba_kolumn


# Wywołanie funkcji
wynik = znajdz_kolumny(czy_przyklad=False)
print(wynik)