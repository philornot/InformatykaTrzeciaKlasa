from interfejs import czytaj_tablice_punktow

lista_z_tuplami_punktow = czytaj_tablice_punktow()


def czy_nalezy_do_okregu(punkty, promien=200, wspolrzedne_srodka=(200, 200)):
    x, y = punkty
    a, b = wspolrzedne_srodka

    if (x - a) ** 2 + (y - b) ** 2 > promien ** 2:
        print(f'\nDla ({x}:{y}) wyrażenie\n'
             f'{(x - a) ** 2 + (y - b) ** 2} jest większe od {promien ** 2}')
        return False

    else:
        return True

licznik = 0
for i in lista_z_tuplami_punktow:
    if czy_nalezy_do_okregu(i):
        licznik += 1

print(f'\n{licznik}')
# print(lista_z_tuplami_punktow)
