from interfejs import czy_pierwsza, czytaj_liczby_z_pliku, odbij_liczbe

odpowiedz = []
liczby = czytaj_liczby_z_pliku(czy_przyklad=False)
for liczba in liczby:
    if czy_pierwsza(liczba) and czy_pierwsza(odbij_liczbe(liczba)):
        odpowiedz.append(liczba)  # print(liczba, odbij_liczbe(liczba))

for i in odpowiedz:
    print(i)
