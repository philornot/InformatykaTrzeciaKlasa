from interfejs import czytaj_liczby_z_pliku

# Pobieramy liczby z pliku
liczby_pierwsze, liczby_calkowite = czytaj_liczby_z_pliku(czy_przyklad=False)

# Sortujemy liczby pierwsze przy użyciu wbudowanej funkcji sorted
posortowane_pierwsze = sorted(liczby_pierwsze, reverse=True)  # odwracamy sortowanie

# Wyświetlamy pozycję sto pierwszą (czyli o indeksie 100, bo pierwsza cyfra ma indeks 0)
print(f'\nOdpowiedź do zadania 4.2:\n{posortowane_pierwsze[100]}')
# fun fact: akurat w tym przypadku dla indeksu 101 też będzie zwracało 1993
