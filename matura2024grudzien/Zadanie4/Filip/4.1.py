from interfejs import odczytaj_wymiary


def oblicz_pole(czy_przyklad=False):
    wysokosc_tabela, szerokosc_tabela = odczytaj_wymiary(czy_przyklad=czy_przyklad)
    pole_tabela = {}
    for j in wysokosc_tabela:
        wysokosc, szerokosc = wysokosc_tabela[j], szerokosc_tabela[j]
        pole_tabela[j] = wysokosc * szerokosc
    return pole_tabela


pola = oblicz_pole(czy_przyklad=False)

pole_maks = 0
for i in pola:
    if pola[i] > pole_maks:
        pole_maks = pola[i]
print(pole_maks)

pole_min = pole_maks
for i in pola:
    if pola[i] < pole_min:
        pole_min = pola[i]
print(pole_min)
