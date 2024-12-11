def silnia_iteracyjna(n):
    # Dla 0! i 1! wynik to 1
    if n <= 1:
        return 1

    # Dla większych liczb mnożymy kolejne liczby
    wynik = 1
    for i in range(2, n + 1):
        wynik = wynik * i

    return wynik


def silnia_rekurencyjna(n):
    # Warunek końcowy rekurencji: 0! = 1 i 1! = 1
    if n <= 1:
        return 1

    # Dla większych liczb: n! = n * (n-1)!
    return n * silnia_rekurencyjna(n - 1)


# Przykład użycia:
# print(silnia_iteracyjna(5))      # Wynik: 120
# print(silnia_rekurencyjna(5))    # Wynik: 120

# Kolejne kroki dla przykładu silnia_iteracyjna(5):
# Start:   wynik = 1
# Krok 1:  i = 2,  wynik = 1 * 2 = 2
# Krok 2:  i = 3,  wynik = 2 * 3 = 6
# Krok 3:  i = 4,  wynik = 6 * 4 = 24
# Krok 4:  i = 5,  wynik = 24 * 5 = 120
# Koniec:  zwracamy 120

# Kolejne kroki dla przykładu silnia_rekurencyjna(5):
# Krok 1:  5 * silnia_rekurencyjna(4)
# Krok 2:  5 * (4 * silnia_rekurencyjna(3))
# Krok 3:  5 * (4 * (3 * silnia_rekurencyjna(2)))
# Krok 4:  5 * (4 * (3 * (2 * silnia_rekurencyjna(1))))
# Krok 5:  5 * (4 * (3 * (2 * 1)))
# Krok 6:  5 * (4 * (3 * 2))
# Krok 7:  5 * (4 * 6)
# Krok 8:  5 * 24
# Koniec:  120

# Czyli:
def silnia(n):
    if n <= 1:
        return 1
    w = 1
    for i in range(2, n + 1):
        w *= i
    return w

# poćwicz ten algorytm, próbując go napisać samemu niżej :)
