from interfejs import czytaj_plik

liczby = czytaj_plik(czy_przyklad=False)
# liczby = [3,7,4,6,10,2,5]
# liczby = [5,70,28,42,98]

def nwd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a


def nwd_dla_n_liczb(*argumenty):
    if len(argumenty) == 1:
        return argumenty[0]
    wynik = argumenty[0]

    for i in range(1, len(argumenty)):
        wynik = nwd(wynik, argumenty[i])
    return wynik



maksymalna_dlugosc = 0
pierwsza_liczba_ciagu = 0
maksymalny_nwd = 0

for i in range(len(liczby)):
    aktualny_nwd = liczby[i]

    for j in range(i + 1, len(liczby)):
        aktualny_nwd = nwd(aktualny_nwd, liczby[j])

        if aktualny_nwd > 1:
            aktualna_dlugosc = j - i + 1
            if aktualna_dlugosc > maksymalna_dlugosc:
                maksymalna_dlugosc = aktualna_dlugosc
                pierwsza_liczba_ciagu = i
                maksymalny_nwd = aktualny_nwd
        else:
            break

pierwsza_liczba = liczby[pierwsza_liczba_ciagu]
dlugosc_ciagu = maksymalna_dlugosc

print(f"Pierwsza liczba ciągu: {pierwsza_liczba}")
print(f"Długość ciągu: {dlugosc_ciagu}")
print(f"Największy wspólny dzielnik: {maksymalny_nwd}")
