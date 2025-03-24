from interfejs import czytaj_plik

punkty = czytaj_plik()

def czy_cyfro_podobne(jakas_liczba1, jakas_liczba2):
    cyfry1 = []
    for cyfra1 in str(jakas_liczba1):
        if cyfra1 not in cyfry1:
            cyfry1.append(cyfra1)

    for cyfra2 in str(jakas_liczba2):
        if cyfra2 not in cyfry1:
            return False

    return True

znalezione = []
for p in punkty:
    liczba1, liczba2 = p
    if czy_cyfro_podobne(liczba1, liczba2):
        znalezione.append(p)

print(len(znalezione))