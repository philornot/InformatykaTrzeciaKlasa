from interfejs import nieparz_skrot

# Pobierz liczbę od użytkownika, którą chcemy skrócić
n = input("Wpisz liczbę n do skrócenia: ")

# Oblicz nieparzysty skrót liczby n za pomocą funkcji nieparz_skrot
m = nieparz_skrot(n)

# Wyświetl wynik
print(f'Nieparzysty skrót liczby {n} to {m}')
