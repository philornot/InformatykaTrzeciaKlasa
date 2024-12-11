def rozklad_na_czynniki(liczba):
    # Tworzymy pustą listę na czynniki pierwsze
    czynniki = []

    # Sprawdzamy kolejne potencjalne dzielniki
    # Zaczynamy od 2 (najmniejszej liczby pierwszej)
    dzielnik = 2

    # Dzielimy liczbę przez kolejne dzielniki, tak długo
    # jak jest większa od 1
    while liczba > 1:
        # Jeśli liczba dzieli się przez aktualny dzielnik
        if liczba % dzielnik == 0:
            # Dodajemy dzielnik do listy czynników
            czynniki.append(dzielnik)
            # Dzielimy liczbę przez znaleziony dzielnik
            liczba = liczba // dzielnik
        else:
            # Jeśli liczba nie dzieli się przez dzielnik
            # przechodzimy do kolejnego
            dzielnik = dzielnik + 1

    return czynniki


# Przykład użycia:
# print(rozklad_na_czynniki(84))  # Wynik: [2, 2, 3, 7]

# Kolejne kroki dla przykładu (84):
# Start:   liczba = 84,  dzielnik = 2,  czynniki = []
# Krok 1:  84 % 2 == 0,  84 // 2 = 42,  czynniki = [2]
# Krok 2:  42 % 2 == 0,  42 // 2 = 21,  czynniki = [2, 2]
# Krok 3:  21 % 2 != 0,  dzielnik = 3
# Krok 4:  21 % 3 == 0,  21 // 3 = 7,   czynniki = [2, 2, 3]
# Krok 5:  7 % 3 != 0,   dzielnik = 4
# Krok 6:  7 % 4 != 0,   dzielnik = 5
# Krok 7:  7 % 5 != 0,   dzielnik = 6
# Krok 8:  7 % 6 != 0,   dzielnik = 7
# Krok 9:  7 % 7 == 0,   7 // 7 = 1,    czynniki = [2, 2, 3, 7]
# Koniec:  zwracamy [2, 2, 3, 7]

# Czyli:
def czynniki(n):
    c = []
    d = 2
    while n > 1:
        if n % d == 0:
            c.append(d)
            n //= d
        else:
            d += 1
    return c

# poćwicz ten algorytm, próbując go napisać samemu niżej :)
