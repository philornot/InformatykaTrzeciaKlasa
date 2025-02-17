from interfejs import czytaj_plik

liczby = czytaj_plik(czy_przyklad=True)

def czy_potega_trojki(liczba):
    if liczba <= 0:
        return False
    while liczba > 1:
        if liczba % 3 != 0:
            return False
        liczba = liczba // 3
    return True

def licz_potegi_trojki(lista_liczb):
    znalezione_potegi = []
    for liczba in lista_liczb:
        if czy_potega_trojki(liczba):
            znalezione_potegi.append(liczba)
    return len(znalezione_potegi)


licznik = licz_potegi_trojki(liczby)
print(licznik)