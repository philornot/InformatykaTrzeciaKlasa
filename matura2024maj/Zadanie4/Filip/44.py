from interfejs import czytaj_liczby_z_pliku

# Pobieramy liczby pierwsze i całkowite z pliku
liczby_pierwsze, liczby_calkowite = czytaj_liczby_z_pliku(czy_przyklad=False)

# Inicjujemy zmienne, które będą przechowywać najwyższą średnią, liczbę elementów w fragmencie i początek fragmentu (indeks)
najwyzsza_srednia = 0  # Najwyższa znaleziona średnia arytmetyczna
najwyzsza_liczba_elementow = 50  # Minimalna liczba elementów zgodnie z poleceniem
najwyzsza_poczatek = -1  # Indeks, od którego zaczyna się fragment z najwyższą średnią (domyślnie -1, bo jeszcze nie znaleziono)

# Pętla przechodzi przez różne rozmiary fragmentów, zaczynając od 50 elementów (bo to minimalny rozmiar fragmentu)
for rozmiar_okna in range(50, len(liczby_pierwsze) + 1):
    # Obliczamy sumę dla pierwszego fragmentu o długości rozmiar_okna (od indeksu 0 do rozmiar_okna)
    suma = sum(liczby_pierwsze[0:rozmiar_okna])

    # Obliczamy średnią dla tego fragmentu
    aktualna_srednia = suma / rozmiar_okna

    # Jeśli aktualna średnia jest większa niż najwyższa znaleziona do tej pory, aktualizujemy zmienne
    if aktualna_srednia > najwyzsza_srednia:
        najwyzsza_srednia = aktualna_srednia
        najwyzsza_poczatek = 0  # Fragment zaczyna się od indeksu 0
        najwyzsza_liczba_elementow = rozmiar_okna  # Ustawiamy aktualny rozmiar okna jako najlepszy

    # Teraz przesuwamy okno (czyli sprawdzamy fragmenty zaczynające się od kolejnych indeksów)
    for i in range(rozmiar_okna, len(liczby_pierwsze)):
        # Aktualizujemy sumę, odejmując wartość liczby, która "wypadła" z okna, i dodając nową liczbę, która "weszła" do okna
        suma = suma + liczby_pierwsze[i] - liczby_pierwsze[i - rozmiar_okna]

        # Obliczamy nową średnią dla przesuniętego fragmentu
        aktualna_srednia = suma / rozmiar_okna

        # Sprawdzamy, czy nowa średnia jest lepsza od najwyższej
        if aktualna_srednia > najwyzsza_srednia:
            najwyzsza_srednia = aktualna_srednia
            najwyzsza_poczatek = i - rozmiar_okna + 1  # Nowy fragment zaczyna się od tego indeksu
            najwyzsza_liczba_elementow = rozmiar_okna  # Aktualizujemy liczbę elementów w najlepszym fragmencie

# Po przejściu przez wszystkie możliwe fragmenty, drukujemy wyniki
print(f'Max średnia: {najwyzsza_srednia}')  # Najwyższa średnia arytmetyczna
print(f'Najwyższa liczba elementów: {najwyzsza_liczba_elementow}')  # Długość fragmentu o najwyższej średniej
print(
    f'Najwyższy początek: {liczby_pierwsze[najwyzsza_poczatek]}')  # Pierwsza liczba w fragmencie o najwyższej średniej
