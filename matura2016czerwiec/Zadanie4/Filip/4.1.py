from interfejs import czytaj_tablice_punktow

lista_z_tuplami_punktow = czytaj_tablice_punktow()


def czy_nalezy_do_brzegu_okregu(punkty, promien=200, wspolrzedne_srodka=(200, 200)):
    x, y = punkty
    a, b = wspolrzedne_srodka
    odleglosc_kw = (x - a) ** 2 + (y - b) ** 2

    # Sprawdzamy czy punkt jest na brzegu
    return abs(odleglosc_kw - promien ** 2) <= 1


def czy_nalezy_do_wnetrza_okregu(punkty, promien=200, wspolrzedne_srodka=(200, 200)):
    x, y = punkty
    a, b = wspolrzedne_srodka
    odleglosc_kw = (x - a) ** 2 + (y - b) ** 2

    # Punkt należy do wnętrza gdy odległość jest mniejsza od promienia
    return odleglosc_kw < promien ** 2


punkty_brzeg = []
punkty_wnetrze = []

for punkt in lista_z_tuplami_punktow:
    if czy_nalezy_do_brzegu_okregu(punkt):
        punkty_brzeg.append(punkt)
    elif czy_nalezy_do_wnetrza_okregu(punkt):
        punkty_wnetrze.append(punkt)

# Wypisujemy punkty na brzegu
for punkt in punkty_brzeg:
    print(f"{punkt[0]} {punkt[1]}")

# Wypisujemy liczbę punktów we wnętrzu
print(f"\n{len(punkty_wnetrze)}")