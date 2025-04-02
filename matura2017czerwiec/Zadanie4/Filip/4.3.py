from interfejs import czytaj_plik

punkty = czytaj_plik()


def licz_odleglosc(punkt_a, punkt_b):
    x_a, y_a = punkt_a
    x_b, y_b = punkt_b
    return int((((x_b - x_a) ** 2) + (y_b - y_a) ** 2) ** (1 / 2))


maks_odleglosc = 0
najdalsze_punkty = (None, None)

for i in range(len(punkty)):
    for j in range(i + 1, len(punkty)):
        odleglosc = licz_odleglosc(punkty[i], punkty[j])
        if odleglosc > maks_odleglosc:
            maks_odleglosc = odleglosc
            najdalsze_punkty = (punkty[i], punkty[j])

print(najdalsze_punkty[0], najdalsze_punkty[1])
print(maks_odleglosc)