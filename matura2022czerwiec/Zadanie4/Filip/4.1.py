from interfejs import czytaj_liczby_z_pliku, czy_podzielna_przez_17, odbij_liczbe

liczby = czytaj_liczby_z_pliku(czy_przyklad=False)
odbite_podzielne_przez_17 = []
for liczba in liczby:
    liczba_odbita = odbij_liczbe(liczba)
    if czy_podzielna_przez_17(liczba_odbita):
        odbite_podzielne_przez_17.append(liczba_odbita)

print("Liczby odbite podzielne przez 17:")
for i in odbite_podzielne_przez_17:
    print(i)
