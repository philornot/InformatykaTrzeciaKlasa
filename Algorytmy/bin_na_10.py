def binarna_na_dziesietna(binarna):
    # Tworzymy zmienną na wynik
    wynik = 0

    # Przechodzimy po każdej cyfrze binarnej od lewej do prawej
    # Każdą cyfrę mnożymy przez odpowiednią potęgę dwójki
    # Przykład dla "1101":
    # 1*2³ + 1*2² + 0*2¹ + 1*2⁰ = 1*8 + 1*4 + 0*2 + 1*1 = 13

    # Zmienna potega to aktualny indeks potęgi liczby 2
    # Dla liczby 4-bitowej będzie to: 3, 2, 1, 0
    potega = len(binarna) - 1

    # Przechodzimy po każdej cyfrze w liczbie binarnej
    for cyfra in binarna:
        # Jeśli cyfra to '1', dodajemy do wyniku 2 do potęgi
        if cyfra == '1':
            # Przykład: dla pierwszej cyfry w "1101"
            # potega = 3, więc 2³ = 8
            wynik = wynik + 2 ** potega

        # Zmniejszamy potęgę o 1 dla kolejnej cyfry
        potega = potega - 1

    return wynik


# Przykład użycia:
# print(binarna_na_dziesietna("1101"))  # Wynik: 13

# Kolejne kroki dla przykładu ("1101"):
# Start:   wynik = 0, potega = 3
# Krok 1:  cyfra = '1', 2³ = 8,     wynik = 0 + 8 = 8
# Krok 2:  cyfra = '1', 2² = 4,     wynik = 8 + 4 = 12
# Krok 3:  cyfra = '0', pomijamy,   wynik = 12
# Krok 4:  cyfra = '1', 2⁰ = 1,     wynik = 12 + 1 = 13
# Koniec:  zwracamy 13

# Czyli:
def na_dec(b):
    w = 0
    p = len(b) - 1
    for c in b:
        if c == '1':
            w += 2 ** p
        p -= 1
    return w

# poćwicz ten algorytm, próbując go napisać samemu niżej :)
