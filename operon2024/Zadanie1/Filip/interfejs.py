def odczytaj_dane(czy_przyklad=False):
    """Bazowa funkcja odczytująca dane z pliku"""
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


def odczytaj_pozycje_i_predkosci(czy_przyklad=False):
    """Funkcja zwracająca dwie tablice: pozycje i prędkości ciężarówek"""
    dane = odczytaj_dane(czy_przyklad)
    n = len(dane)
    pozycje = [0] * n
    predkosci = [0] * n

    for i in range(n):
        km, v = dane[i].split()
        pozycje[i] = int(km)
        predkosci[i] = int(v)

    return pozycje, predkosci


def odczytaj_czasy_przejazdu(czy_przyklad=False):
    """Funkcja zwracająca tablicę czasów przejazdu dla każdej ciężarówki"""
    pozycje, predkosci = odczytaj_pozycje_i_predkosci(czy_przyklad)
    n = len(pozycje)
    czasy = [0] * n

    for i in range(n):
        czasy[i] = pozycje[i] / predkosci[i]

    return czasy