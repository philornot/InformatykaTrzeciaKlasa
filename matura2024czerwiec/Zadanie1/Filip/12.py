from matura2024czerwiec.Zadanie1.Filip.interfejs import zamien_na_bin


def znajdz_cyfre_w_rogu(w, k, n):
    """
    Znajduje cyfrę w prawym dolnym rogu tablicy w×k,
    do której wpisano liczbę binarną n.

    :param w: liczba wierszy tablicy
    :type w: int
    :param k: liczba kolumn tablicy
    :type k: int
    :param n: liczba dodatnia do zapisania w systemie binarnym
    :type n: int
    :return: cyfra (0 lub 1) znajdująca się w prawym dolnym rogu tablicy
    :rtype: int

    :note:
    Liczba binarna jest wpisywana do tablicy wiersz po wierszu, od lewej do prawej.
    Gdy skończą się cyfry liczby binarnej, zaczynamy wpisywanie od początku.
    """

    # Zamieniamy liczbę na postać binarną używając dostarczonej funkcji
    binary = zamien_na_bin(n)
    # Uzupełniamy zerami z przodu, aby długość była w*k
    binary = '0' * (w * k - len(binary)) + binary

    # Tworzymy tablicę w×k wypełnioną zerami
    tablica = [[0 for _ in range(k)] for _ in range(w)]

    # Indeks aktualnie wstawianej cyfry z liczby binarnej
    idx = 0

    # Wypełniamy tablicę zgodnie z regułami:
    # 1. Najpierw pierwszy wiersz od lewej do prawej
    # 2. Potem drugi wiersz od lewej do prawej itd.
    # 3. Jeśli skończą się cyfry, zaczynamy od początku

    for i in range(w):  # dla każdego wiersza
        for j in range(k):  # dla każdej kolumny
            # Jeśli wyczerpaliśmy wszystkie cyfry, zaczynamy od początku
            if idx >= len(binary):
                idx = 0

            # Wstawiamy kolejną cyfrę do tablicy
            tablica[i][j] = int(binary[idx])

            # Przechodzimy do następnej cyfry
            idx += 1

    # Zwracamy cyfrę z prawego dolnego rogu
    return tablica[w - 1][k - 1]


# Przykład użycia dla danych z zadania przykładowego:
# w = 5, k = 3, n = 19 (binarnie: 10011)
wynik = znajdz_cyfre_w_rogu(5, 3, 19)
print(f"Cyfra w prawym dolnym rogu: {wynik}")  # Powinno wypisać: 1

# Test dla innych danych:
test_cases = [(5, 3, 19),  # przykład z zadania
              (2, 2, 3),  # mała tablica
              (3, 4, 15),  # inna liczba
              ]

for w, k, n in test_cases:
    binary = zamien_na_bin(n)
    print(f"Dla w={w}, k={k}, n={n} (bin={binary})")
    wynik = znajdz_cyfre_w_rogu(w, k, n)
    print(f"Cyfra w prawym dolnym rogu: {wynik}")
    print()
