from interfejs import czytaj_plik

def nwd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a

liczby = czytaj_plik(czy_przyklad=True)

def nwd_dla_n_liczb(*n):
    nwd(n, n[:-1])

nwd_dla_n_liczb(70, 28, 42, 98)