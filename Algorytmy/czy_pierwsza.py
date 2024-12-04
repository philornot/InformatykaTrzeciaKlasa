def czy_pierwsza(liczba):
    # Liczby mniejsze niż 2 nie są pierwsze
    if liczba < 2:
        return False

    # Sprawdzamy wszystkie potencjalne dzielniki od 2 do pierwiastka z liczby
    # Wystarczy sprawdzić do pierwiastka, bo jeśli liczba nie jest pierwsza,
    # to musi mieć dzielnik mniejszy lub równy pierwiastkowi z niej
    # Przykład: dla 100 = 10 * 10 wystarczy sprawdzić do 10

    # Nie używamy pierwiastka (sqrt), tylko porównujemy kwadrat i
    i = 2
    while i * i <= liczba:
        # Jeśli liczba dzieli się przez i, to nie jest pierwsza
        if liczba % i == 0:
            return False
        i = i + 1

    # Jeśli żaden dzielnik nie został znaleziony, liczba jest pierwsza
    return True


# Przykład użycia:
# print(czy_pierwsza(17))  # Wynik: True
# print(czy_pierwsza(24))  # Wynik: False

# Kolejne kroki dla przykładu (17):
# Start:   liczba = 17
# Krok 1:  i = 2,  2 * 2 = 4 <= 17,   17 % 2 != 0
# Krok 2:  i = 3,  3 * 3 = 9 <= 17,   17 % 3 != 0
# Krok 3:  i = 4,  4 * 4 = 16 <= 17,  17 % 4 != 0
# Krok 4:  i = 5,  5 * 5 = 25 > 17,   kończymy
# Koniec:  zwracamy True (żaden dzielnik nie znaleziony)

# Kolejne kroki dla przykładu (24):
# Start:   liczba = 24
# Krok 1:  i = 2,  2 * 2 = 4 <= 24,   24 % 2 == 0
# Koniec:  zwracamy False (znaleziony dzielnik)

# Czyli:
def pierwsza(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

# poćwicz ten algorytm, próbując go napisać samemu niżej :)
