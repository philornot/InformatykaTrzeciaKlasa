from interfejs import czytaj_plik

liczby = czytaj_plik(czy_przyklad=False)

def czy_potega_trojki(liczba):
    potega_trojki = 1
    while liczba > potega_trojki:
        potega_trojki *= 3
        if potega_trojki == liczba:
            return True
    return False

def licz_potegi_trojki(lista_liczb):
    znalezione_potegi = []
    for liczba in lista_liczb:
        if czy_potega_trojki(liczba):
            znalezione_potegi.append(liczba)
    return len(znalezione_potegi)


licznik = licz_potegi_trojki(liczby)
print(licznik)
