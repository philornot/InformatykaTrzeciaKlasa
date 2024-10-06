def czytaj_liczby_z_pliku(plik="../../../matura2024maj/dane2024maj/liczby.txt"):
    # Otwieramy plik do odczytu, wiersze to linie z pliku
    with open(plik, encoding="utf-8") as f:
        wiersze = f.readlines()

    # Dzielimy pierwszy i drugi wiersz po spacji, żeby uzyskać listę liczb (w formacie string)
    liczby_pierwsze_string = wiersze[0].strip().split(' ')
    liczby_calkowite_string = wiersze[1].strip().split(' ')

    # Te listy będą przechowywać liczby jako inty, bo potrzebujemy ich do obliczeń
    liczby_pierwsze = []
    liczby_calkowite = []

    # Zamieniamy liczby z pierwszego wiersza (które są stringami) na liczby całkowite (int)
    for liczba_pierwsza in liczby_pierwsze_string:
        liczby_pierwsze.append(int(liczba_pierwsza))

    # To samo robimy z liczbami z drugiego wiersza
    for liczba_calkowita in liczby_calkowite_string:
        liczby_calkowite.append(int(liczba_calkowita))

    # Zwracamy dwie listy: liczby pierwsze i liczby całkowite
    return liczby_pierwsze, liczby_calkowite
