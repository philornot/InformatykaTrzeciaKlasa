def czy_palindrom(tekst):
    # Przechodzimy jednocześnie od początku i od końca
    # Wystarczy sprawdzić do połowy tekstu
    # Porównujemy czy znaki są takie same

    # i idzie od początku, j od końca
    i = 0
    j = len(tekst) - 1

    # Sprawdzamy, dopóki i nie minie j
    while i < j:
        # Jeśli znaki są różne, to nie palindrom
        if tekst[i] != tekst[j]:
            return False
        i = i + 1
        j = j - 1

    # Jeśli doszliśmy tutaj, to palindrom
    return True


# Przykład użycia:
# print(czy_palindrom("kajak"))     # Wynik: True
# print(czy_palindrom("python"))    # Wynik: False

# Kolejne kroki dla przykładu "kajak":
# Start:   i = 0, j = 4
# Krok 1:  tekst[0] = 'k', tekst[4] = 'k', i = 1, j = 3
# Krok 2:  tekst[1] = 'a', tekst[3] = 'a', i = 2, j = 2
# Koniec:  i >= j, więc zwracamy True

# Kolejne kroki dla przykładu "python":
# Start:   i = 0, j = 5
# Krok 1:  tekst[0] = 'p', tekst[5] = 'n', różne!
# Koniec:  zwracamy False

# Czyli:
def palindrom(t):
    i = 0
    j = len(t) - 1
    while i < j:
        if t[i] != t[j]:
            return False
        i += 1
        j -= 1
    return True

# poćwicz ten algorytm, próbując go napisać samemu niżej :)
