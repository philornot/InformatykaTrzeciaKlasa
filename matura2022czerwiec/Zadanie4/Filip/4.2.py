from interfejs import czytaj_liczby_z_pliku, odbij_liczbe

liczby = czytaj_liczby_z_pliku(czy_przyklad=False)
maks_abs_roznicy = 0, 0
for liczba in liczby:
    abs_roznicy = abs(liczba - odbij_liczbe(liczba))
    if abs_roznicy > maks_abs_roznicy[0]:
        maks_abs_roznicy= liczba, abs_roznicy


print(maks_abs_roznicy)
