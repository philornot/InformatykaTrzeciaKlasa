def nwd_euklides(a, b):
    # Algorytm działa, dopóki b nie jest równe 0
    # Gdy b == 0, wtedy a zawiera wynik (NWD)
    while b != 0:
        # Zapamiętujemy aktualną wartość b,
        # bo za chwilę zostanie nadpisana
        temp = b

        # Obliczamy resztę z dzielenia a przez b
        # To jest kluczowy krok algorytmu Euklidesa
        # Przykład: dla a=48, b=18:
        # 48 ÷ 18 = 2 reszta 12, więc b = 12
        b = a % b

        # Poprzednią wartość b (zapisaną w temp)
        # przypisujemy do a
        # Przykład: dla a=48, b=18:
        # temp = 18, więc teraz a = 18
        a = temp

    # Gdy b == 0, wartość a zawiera NWD
    return a


# Przykład użycia:
# print(nwd_euklides(48, 18))  # Wynik: 6

# Kolejne kroki dla przykładu (48, 18):
# Start:   a = 48, b = 18
# Krok 1:  a = 18, b = 12  (48 % 18 = 12)
# Krok 2:  a = 12, b = 6   (18 % 12 = 6)
# Krok 3:  a = 6,  b = 0

# Czyli:
def nwd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a

# poćwicz ten algorytm, próbując go napisać samemu niżej :)
