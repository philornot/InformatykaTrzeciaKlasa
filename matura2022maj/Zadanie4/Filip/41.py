from interfejs import czytaj_plik, przyklad_txt

liczby = czytaj_plik(plik=przyklad_txt)
for liczba in liczby:
    liczba = str(liczba)
    print(liczba[0])
