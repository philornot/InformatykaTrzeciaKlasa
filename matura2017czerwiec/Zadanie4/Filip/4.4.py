from interfejs import czytaj_plik

punkty = czytaj_plik()

bok_kwadratu = 10000
y_min_kwadratu = -bok_kwadratu/2
x_min_kwadratu = -bok_kwadratu/2
y_maks_kwadratu = bok_kwadratu/2 # uzyj mnieee
x_maks_kwadratu = bok_kwadratu/2


# jego środek jest w (0,0)
# czyli ma wierzchołki w (-5000, -5000), (-5000, 5000), (500, 5000), (500, -5000)


def czy_nalezy_do_kwadratu(punkt):
    x, y = punkt
    if x == x_min_kwadratu:
        print(f'Warunek 1 spełniony dla {punkt}')
        if y >= -5000:
            print(f'Warunek 2 spełniony dla {punkt}')
            if y <= 5000:
                print(f'Warunek 3 spełniony dla {punkt}')
                return True
    elif y == -5000:
        print(f'Warunek 1 spełniony dla {punkt}')
        if x >= -5000:
            print(f'Warunek 2 spełniony dla {punkt}')
            if x <= 5000:
                print(f'Warunek 3 spełniony dla {punkt}')
                return True
    else:
        return False

for punkt in punkty:
    x, y = punkt
    if x == 5000:
        print(punkt)
    if czy_nalezy_do_kwadratu(punkt):
        print(punkt)
