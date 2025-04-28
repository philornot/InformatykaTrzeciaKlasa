from interfejs import czytaj_dane

napisy = czytaj_dane(czy_przyklad=False)

licznik = 0
for napis in napisy:
    for znak in napis:
        if znak in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            licznik += 1

print(licznik)
