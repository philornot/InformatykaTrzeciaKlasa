from interfejs import czytaj_liczby_z_pliku, rozklad_na_czynniki

# Pobieramy liczby z pliku, z opcją na wybór pliku przykładowego (tu ustawiamy na False, żeby korzystać z pełnego pliku)
liczby_pierwsze, liczby_calkowite = czytaj_liczby_z_pliku(czy_przyklad=False)

# Wyświetlamy odpowiedź dla zadania 4.3
print('\nOdpowiedź do zadania 4.3:')

# Przechodzimy przez każdą liczbę całkowitą z drugiego wiersza
for liczba_calkowita in liczby_calkowite:
    # Rozkładamy liczbę całkowitą na czynniki pierwsze (zwróci listę czynników)
    czynniki = rozklad_na_czynniki(liczba_calkowita)

    # Robimy kopię listy liczb pierwszych, żeby móc usuwać z niej elementy (bez modyfikacji oryginału)
    liczby_pierwsze_kopia = liczby_pierwsze.copy()

    # Zmienna logiczna, która będzie mówić, czy wszystkie czynniki liczby są liczbami pierwszymi
    czy_sie_uda = True

    # Przechodzimy przez każdy czynnik rozłożonej liczby całkowitej
    for czynnik in czynniki:
        # Sprawdzamy, czy dany czynnik jest w liście liczb pierwszych
        if czynnik not in liczby_pierwsze_kopia:
            # Jeśli nie ma takiego czynnika, przerywamy pętlę i ustawiamy flagę na False
            czy_sie_uda = False
            break
        else:
            # Jeśli czynnik istnieje, usuwamy go z kopii listy liczb pierwszych (żeby nie użyć go więcej razy)
            liczby_pierwsze_kopia.remove(czynnik)

    # Jeśli wszystkie czynniki były liczbami pierwszymi, wypisujemy liczbę całkowitą
    if czy_sie_uda:
        print(liczba_calkowita)
