def czytaj_liczby_z_pliku(czy_przyklad=False):
    # Sprawdzamy, z którego pliku mamy korzystać: jeśli True, korzystamy z pliku przykładowego, w przeciwnym wypadku z pełnego pliku
    if czy_przyklad is True:
        plik = "../../../matura2024maj/dane2024maj/liczby_przyklad.txt"
    else:
        plik = "../../../matura2024maj/dane2024maj/liczby.txt"

    # Otwieramy plik do odczytu i pobieramy jego wiersze
    with open(plik, encoding="utf-8") as f:
        wiersze = f.readlines()

    # Zamieniamy pierwszy i drugi wiersz na listy stringów (rozdzielając po spacji)
    liczby_pierwsze_string = wiersze[0].strip().split(' ')
    liczby_calkowite_string = wiersze[1].strip().split(' ')

    # Puste listy, do których będą trafić liczby jako inty
    liczby_pierwsze = []
    liczby_calkowite = []

    # Zamieniamy liczby pierwsze z wiersza na inty i dodajemy do listy
    for liczba_pierwsza in liczby_pierwsze_string:
        liczby_pierwsze.append(int(liczba_pierwsza))

    # To samo robimy z liczbami całkowitymi z drugiego wiersza
    for liczba_calkowita in liczby_calkowite_string:
        liczby_calkowite.append(int(liczba_calkowita))

    # Zwracamy obie listy: liczby pierwsze i liczby całkowite
    return liczby_pierwsze, liczby_calkowite


def rozklad_na_czynniki(n):
    # Lista do przechowywania czynników
    czynniki = []
    i = 2  # Zaczynamy od najmniejszej liczby pierwszej (2)

    # Pętla, dopóki i^2 <= n (nie ma sensu sprawdzać większych, bo to będą liczby większe niż połowa n)
    while i * i <= n:
        # Dopóki n jest podzielne przez i, dodajemy i do listy czynników i dzielimy n przez i
        while n % i == 0:
            czynniki.append(i)
            n = n // i
        i = i + 1  # Zwiększamy i

    # Jeśli na koniec n > 1, oznacza to, że n samo w sobie jest liczbą pierwszą, więc dodajemy je do listy czynników
    if n > 1:
        czynniki.append(n)

    # Zwracamy listę czynników pierwszych
    return czynniki
