def dziesietna_na_binarna(liczba):
    # Jeśli liczba jest zerem, od razu zwracamy "0"
    if liczba == 0:
        return "0"

    # Tworzymy pustego stringa na wynik
    wynik = ""

    # Wykonujemy dzielenie przez 2, dopóki liczba nie będzie zerem
    # W każdym kroku dopisujemy resztę z dzielenia (0 lub 1) na początku wyniku
    while liczba > 0:
        # Obliczamy resztę z dzielenia przez 2 (będzie to 0 lub 1)
        # Przykład: dla 13:
        # 13 % 2 = 1 (bo 13 = 6 * 2 + 1)
        reszta = liczba % 2

        # Dodajemy resztę na początku wyniku
        # (zamieniamy też liczbę na string przez str())
        wynik = str(reszta) + wynik

        # Dzielimy liczbę przez 2 (dzielenie całkowite)
        # Przykład: dla 13:
        # 13 // 2 = 6
        liczba = liczba // 2

    # Zwracamy wynik jako string
    return wynik


# Przykład użycia:
# print(dziesietna_na_binarna(13))  # Wynik: "1101"

# Kolejne kroki dla przykładu (13):
# Start:   liczba = 13    wynik = ""
# Krok 1:  13 % 2 = 1     wynik = "1"       liczba = 6
# Krok 2:  6 % 2 = 0      wynik = "01"      liczba = 3
# Krok 3:  3 % 2 = 1      wynik = "101"     liczba = 1
# Krok 4:  1 % 2 = 1      wynik = "1101"    liczba = 0
# Koniec:  zwracamy "1101"

# Czyli:
def na_bin(n):
    if n == 0:
        return "0"
    w = ""
    while n > 0:
        w = str(n % 2) + w
        n //= 2
    return w

# poćwicz ten algorytm, próbując go napisać samemu niżej :)
