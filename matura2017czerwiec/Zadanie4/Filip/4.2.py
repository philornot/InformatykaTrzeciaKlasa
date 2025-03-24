from interfejs import czytaj_plik

punkty = czytaj_plik()


def czy_cyfro_podobne(jakas_liczba1, jakas_liczba2):
    str_liczba1 = str(jakas_liczba1)
    str_liczba2 = str(jakas_liczba2)

    cyfry1 = set(str_liczba1)
    cyfry2 = set(str_liczba2)

    return cyfry1 == cyfry2


znalezione = []
for p in punkty:
    liczba1, liczba2 = p
    if czy_cyfro_podobne(liczba1, liczba2):
        znalezione.append(p)

print(len(znalezione))
for i, punkt in enumerate(znalezione[:5]):
    print(punkt)