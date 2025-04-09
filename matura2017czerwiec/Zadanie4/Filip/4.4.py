from interfejs import czytaj_plik

punkty = czytaj_plik()

# kwadrat ma środek w (0,0)
# czyli ma wierzchołki w (-5000, -5000), (-5000, 5000), (5000, 5000), (5000, -5000)

bok_kwadratu = 10000
y_min_kwadratu = -bok_kwadratu / 2
x_min_kwadratu = -bok_kwadratu / 2
y_maks_kwadratu = bok_kwadratu / 2
x_maks_kwadratu = bok_kwadratu / 2

wewnatrz = 0
na_bokach = 0
na_zewnatrz = 0


def czy_nalezy_do_kwadratu(punkt):
    x, y = punkt

    # sprawdź czy punkt leży na którymś z boków
    na_lewym_boku = (x == x_min_kwadratu and y_min_kwadratu <= y <= y_maks_kwadratu)
    na_prawym_boku = (x == x_maks_kwadratu and y_min_kwadratu <= y <= y_maks_kwadratu)
    na_dolnym_boku = (y == y_min_kwadratu and x_min_kwadratu <= x <= x_maks_kwadratu)
    na_gornym_boku = (y == y_maks_kwadratu and x_min_kwadratu <= x <= x_maks_kwadratu)

    if na_lewym_boku or na_prawym_boku or na_dolnym_boku or na_gornym_boku:
        return "na boku"

    # sprawdź, czy punkt leży wewnątrz kwadratu
    elif x_min_kwadratu < x < x_maks_kwadratu and y_min_kwadratu < y < y_maks_kwadratu:
        return "wewnątrz"

    # jeśli wszystko wyżej jest False, to punkt musi leżeć na zewnątrz
    else:
        return "na zewnątrz"


for punkt in punkty:
    wynik = czy_nalezy_do_kwadratu(punkt)
    if wynik == "wewnątrz":
        wewnatrz += 1
    elif wynik == "na boku":
        na_bokach += 1
    else:
        na_zewnatrz += 1

odpowiedz = f'\n\n========\nZadanie 4.4:\na. {wewnatrz}\nb. {na_bokach}\nc. {na_zewnatrz}'
with open('wyniki4.txt', 'a') as f:
    f.write(odpowiedz)