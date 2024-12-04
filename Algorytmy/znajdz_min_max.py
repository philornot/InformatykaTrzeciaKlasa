def znajdz_najwiekszy(tablica):
    # Zakładamy, że pierwszy element jest największy
    najwiekszy = tablica[0]

    # Przechodzimy przez pozostałe elementy
    for i in range(1, len(tablica)):
        # Jeśli znajdziemy większy element
        # aktualizujemy największy
        if tablica[i] > najwiekszy:
            najwiekszy = tablica[i]

    return najwiekszy


def znajdz_najmniejszy(tablica):
    # Zakładamy, że pierwszy element jest najmniejszy
    najmniejszy = tablica[0]

    # Przechodzimy przez pozostałe elementy
    for i in range(1, len(tablica)):
        # Jeśli znajdziemy mniejszy element
        # aktualizujemy najmniejszy
        if tablica[i] < najmniejszy:
            najmniejszy = tablica[i]

    return najmniejszy


# Przykład użycia:
# t = [4, 7, 2, 8, 1, 3, 5]
# print(znajdz_najwiekszy(t))  # Wynik: 8
# print(znajdz_najmniejszy(t)) # Wynik: 1

# Kolejne kroki dla przykładu znajdz_najwiekszy([4, 7, 2, 8, 1, 3, 5]):
# Start:   najwiekszy = 4
# Krok 1:  7 > 4,    najwiekszy = 7
# Krok 2:  2 < 7,    najwiekszy = 7
# Krok 3:  8 > 7,    najwiekszy = 8
# Krok 4:  1 < 8,    najwiekszy = 8
# Krok 5:  3 < 8,    najwiekszy = 8
# Krok 6:  5 < 8,    najwiekszy = 8
# Koniec:  zwracamy 8

# Czyli:
def max_element(t):
    m = t[0]
    for x in t:
        if x > m:
            m = x
    return m


def min_element(t):
    m = t[0]
    for x in t:
        if x < m:
            m = x
    return m

# poćwicz ten algorytm, próbując go napisać samemu niżej :)
