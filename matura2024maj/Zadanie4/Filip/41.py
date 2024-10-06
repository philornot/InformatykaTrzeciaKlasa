from interfejs import czytaj_liczby_z_pliku

# Pobieramy liczby z pliku (dwie listy: liczby pierwsze i liczby całkowite)
liczby_pierwsze, liczby_calkowite = czytaj_liczby_z_pliku(czy_przyklad=False)

# Zmienna do przechowywania ilości liczb pierwszych, które są dzielnikami jakiejś liczby z drugiego wiersza
ile_liczb_z_dzielnikiem = 0

# Przechodzimy przez każdą liczbę pierwszą z listy
for liczba_pierwsza in liczby_pierwsze:
    # Dla każdej liczby pierwszej sprawdzamy każdą liczbę całkowitą z drugiego wiersza
    for liczba_calkowita in liczby_calkowite:
        # Sprawdzamy, czy liczba całkowita dzieli się bez reszty przez liczbę pierwszą
        if liczba_calkowita % liczba_pierwsza == 0:
            # Jeśli tak, zwiększamy licznik i przerywamy wewnętrzną pętlę (bo wystarczy jedna zgodność)
            ile_liczb_z_dzielnikiem += 1
            break  # Wychodzimy z pętli, nie musimy dalej sprawdzać tej liczby pierwszej

# Wyświetlamy odpowiedź na zadanie 4.1
print(f'\nOdpowiedź do 4.1:\n{ile_liczb_z_dzielnikiem}')
