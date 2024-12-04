def nwd(a, b):
    # Potrzebujemy NWD do obliczenia NWW
    # To ten sam algorytm Euklidesa co wcześniej
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a


def nww_przez_nwd(a, b):
    # NWW obliczamy ze wzoru: NWW(a,b) = (a*b)/NWD(a,b)
    # Najpierw mnożymy liczby, potem dzielimy przez ich NWD
    return (a * b) // nwd(a, b)


# Przykład użycia:
# print(nww_przez_nwd(12, 18))  # Wynik: 36

# Kolejne kroki dla przykładu (12, 18):
# 1. Obliczamy NWD(12, 18):
#    Start:   a = 12, b = 18
#    Krok 1:  a = 18, b = 12  (12 % 18 = 12)
#    Krok 2:  a = 12, b = 6   (18 % 12 = 6)
#    Krok 3:  a = 6,  b = 0   (12 % 6 = 0)
#    NWD = 6
#
# 2. Obliczamy NWW:
#    NWW = (12 * 18) // 6
#    NWW = 216 // 6 = 36

# Można też napisać NWW bez użycia NWD,
# ale będzie to mniej wydajne:
def nww_przez_wielokrotnosci(a, b):
    # Zaczynamy od większej z liczb
    if a > b:
        wynik = a
    else:
        wynik = b

    # Zwiększamy wynik, aż znajdziemy liczbę
    # podzielną przez obie liczby
    while True:
        if wynik % a == 0 and wynik % b == 0:
            return wynik
        wynik += 1


# Czyli najkrócej:
def nww(a, b):
    return (a * b) // nwd(a, b)

# poćwicz ten algorytm, próbując go napisać samemu niżej :)
