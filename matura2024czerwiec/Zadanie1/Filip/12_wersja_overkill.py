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


def main():
    print("Podaj wymiary tablicy:")

    try:
        w = wczytaj_liczbe_naturalna("Liczba wierszy (w): ")
        k = wczytaj_liczbe_naturalna("Liczba kolumn (k): ")

        max_liczba = sprawdz_max_liczbe(w, k)

        while True:
            try:
                n = wczytaj_liczbe_naturalna(f"Podaj liczbę do zamiany na binarną (n): ")
                if n > max_liczba:
                    raise ValueError(f"Liczba jest za duża! Maksymalna dozwolona liczba dla tabeli {w}×{k} to {max_liczba}\n" +
                                     f"(jej zapis binarny ma dokładnie {w * k} cyfr)")
                break
            except ValueError as e:
                print(f"Błąd: {e}")

        binary = zamien_na_bin(n)
        binary = '0' * (w * k - len(binary)) + binary

        tablica = [[0 for _ in range(k)] for _ in range(w)]
        idx = 0

        for i in range(w):
            for j in range(k):
                if idx >= len(binary):
                    idx = 0
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
