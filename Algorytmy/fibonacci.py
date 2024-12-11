def fib_iteracyjny(n):
    # Dla n <= 1 zwracamy n (czyli 0->0, 1->1)
    if n <= 1:
        return n

    # Dla większych liczb potrzebujemy dwie poprzednie
    # aby obliczyć kolejną
    a = 0  # F(0)
    b = 1  # F(1)

    # Obliczamy kolejne liczby od F(2) do F(n)
    for i in range(2, n + 1):
        # Kolejna liczba to suma dwóch poprzednich
        # Przed przypisaniem nowej wartości do b
        # musimy zachować starą wartość b w temp
        temp = b
        b = a + b
        a = temp

    return b


def fib_rekurencyjny(n):
    # Warunek końcowy rekurencji
    if n <= 1:
        return n

    # F(n) = F(n-1) + F(n-2)
    return fib_rekurencyjny(n - 1) + fib_rekurencyjny(n - 2)


# Przykład użycia:
# print(fib_iteracyjny(6))     # Wynik: 8
# print(fib_rekurencyjny(6))   # Wynik: 8

# Kolejne kroki dla przykładu fib_iteracyjny(6):
# Start:   a = 0, b = 1
# Krok 1:  i = 2,  temp = 1, b = 0 + 1 = 1, a = 1
# Krok 2:  i = 3,  temp = 1, b = 1 + 1 = 2, a = 1
# Krok 3:  i = 4,  temp = 2, b = 1 + 2 = 3, a = 2
# Krok 4:  i = 5,  temp = 3, b = 2 + 3 = 5, a = 3
# Krok 5:  i = 6,  temp = 5, b = 3 + 5 = 8, a = 5
# Koniec:  zwracamy 8

# Kolejne kroki dla przykładu fib_rekurencyjny(6):
# F(6) = F(5) + F(4)
# F(5) = F(4) + F(3)
# F(4) = F(3) + F(2)
# F(3) = F(2) + F(1)
# F(2) = F(1) + F(0)
# F(1) = 1
# F(0) = 0

# Czyli:
def fib(n):
    if n <= 1:
        return n
    a = 0
    b = 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b

# poćwicz ten algorytm, próbując go napisać samemu niżej :)
