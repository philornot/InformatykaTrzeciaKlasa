from matura2024czerwiec.Zadanie1.Filip.interfejs import zamien_na_bin


def rysuj_tablice(tablica):
    w = len(tablica)
    k = len(tablica[0])

    print('┌' + '───┬' * (k - 1) + '───┐')

    for i in range(w):
        print('│', end='')
        for j in range(k):
            print(f' {tablica[i][j]} │', end='')
        print()

        if i < w - 1:
            print('├' + '───┼' * (k - 1) + '───┤')

    print('└' + '───┴' * (k - 1) + '───┘')


def sprawdz_max_liczbe(w, k):
    return (2 ** (w * k)) - 1


def czy_liczba_naturalna(tekst):
    if not tekst:  # pusty string
        return False

    dozwolone_znaki = '0123456789'
    for znak in tekst:
        if znak not in dozwolone_znaki:
            return False
    return True


def wczytaj_liczbe_naturalna(prompt):
    while True:
        try:
            liczba = input(prompt)
            if not czy_liczba_naturalna(liczba):
                raise ValueError("Liczba musi być dodatnia i całkowita!")
            liczba = int(liczba)
            if liczba <= 0:
                raise ValueError("Liczba musi być większa od 0!")
            return liczba
        except ValueError as e:
            print(f"Błąd: {e}")


def oblicz_wymiary(bin_length):
    """Oblicza optymalne wymiary tablicy dla danej długości liczby binarnej."""
    if bin_length == 1:
        return 1, 1

    # Znajdujemy przybliżony pierwiastek bez użycia math.sqrt
    w = 1
    while w * w <= bin_length:
        w += 1
    w -= 1

    # Znajdujemy najbliższy dzielnik
    while bin_length % w != 0 and w > 0:
        w -= 1

    if w == 0:  # Jeśli nie znaleziono dzielnika
        w = 1

    k = bin_length // w
    if bin_length % w != 0:
        k += 1

    return w, k


def main():
    print("Program do tworzenia tablicy binarnej.")
    print("Naciśnij Enter przy wymiarach, aby użyć automatycznych wymiarów.\n")

    try:
        # Wczytywanie wymiarów (opcjonalne)
        w_input = input("Liczba wierszy (w) [Enter dla auto]: ").strip()
        k_input = input("Liczba kolumn (k) [Enter dla auto]: ").strip()

        # Flaga określająca, czy wymiary są automatyczne
        auto_dimensions = not (w_input and k_input)

        # Jeśli podano wymiary, sprawdź ich poprawność
        if not auto_dimensions:
            if not czy_liczba_naturalna(w_input) or not czy_liczba_naturalna(k_input):
                raise ValueError("Wymiary muszą być liczbami naturalnymi!")
            w = int(w_input)
            k = int(k_input)
            if w <= 0 or k <= 0:
                raise ValueError("Wymiary muszą być większe od 0!")

        # Wczytaj liczbę do konwersji
        while True:
            try:
                n = wczytaj_liczbe_naturalna(f"Podaj liczbę do zamiany na binarną (n): ")
                binary = zamien_na_bin(n)

                if auto_dimensions:
                    # Oblicz optymalne wymiary dla danej liczby binarnej
                    w, k = oblicz_wymiary(len(binary))
                    print(f"\nAutomatycznie dobrane wymiary: {w}×{k}")
                else:
                    # Sprawdź czy liczba nie jest za duża dla podanych wymiarów
                    max_liczba = sprawdz_max_liczbe(w, k)
                    if n > max_liczba:
                        raise ValueError(
                            f"Liczba jest za duża! Maksymalna dozwolona liczba dla tabeli {w}×{k} to {max_liczba}")

                break
            except ValueError as e:
                print(f"Błąd: {e}")

        # Dopełnij zapis binarny zerami
        binary = '0' * (w * k - len(binary)) + binary

        # Utworzenie i wypełnienie tablicy
        tablica = [[0 for _ in range(k)] for _ in range(w)]
        idx = 0

        for i in range(w):
            for j in range(k):
                if idx < len(binary):
                    tablica[i][j] = int(binary[idx])
                    idx += 1

        print(f"\nLiczba {n} w systemie binarnym: {binary}")
        print(f"Długość zapisu binarnego: {len(binary)} cyfr")
        print(f"\nTablica {w}×{k}:")
        rysuj_tablice(tablica)
        print(f"\nCyfra w prawym dolnym rogu: {tablica[w - 1][k - 1]}")

    except KeyboardInterrupt:
        print("\nProgram zakończony przez użytkownika.")
    except Exception as e:
        print(f"\nWystąpił nieoczekiwany błąd: {e}")


if __name__ == "__main__":
    main()
