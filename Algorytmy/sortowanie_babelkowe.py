def sortowanie_babelkowe(lista):
    # Pobieramy długość listy, żeby wiedzieć ile elementów musimy posortować
    n = len(lista)

    # Zewnętrzna pętla kontroluje liczbę "przejść" przez listę
    # Dla n elementów, potrzebujemy maksymalnie n-1 przejść
    for i in range(n - 1):
        # Flaga informująca czy w danym przejściu nastąpiła zamiana
        # Jeśli nie, to lista jest już posortowana i możemy zakończyć wcześniej
        zamiana = False

        # Wewnętrzna pętla - przechodzi przez pary sąsiednich elementów
        # Z każdym przejściem zmniejszamy zakres o i, bo największe elementy
        # są już na swoich miejscach na końcu listy
        for j in range(0, n - i - 1):
            # Porównujemy sąsiednie elementy
            if lista[j] > lista[j + 1]:
                # Jeśli elementy są w złej kolejności, zamieniamy je miejscami
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                # Nastąpiła zamiana, więc ustawiamy flagę
                zamiana = True

        # Jeśli nie było żadnej zamiany, lista jest już posortowana
        if not zamiana:
            break

    return lista


# Przykład użycia:
# print(sortowanie_babelkowe([64, 34, 25, 12, 22, 11, 90]))  # Wynik: [11, 12, 22, 25, 34, 64, 90]

# Kolejne kroki dla przykładu [64, 34, 25, 12, 22, 11, 90]:
# Start:   lista = [64, 34, 25, 12, 22, 11, 90]
# Przejście 1:
#   j=0: [64,34] -> zamiana -> [34,64]
#        lista = [34, 64, 25, 12, 22, 11, 90]
#   j=1: [64,25] -> zamiana -> [25,64]
#        lista = [34, 25, 64, 12, 22, 11, 90]
#   j=2: [64,12] -> zamiana -> [12,64]
#        lista = [34, 25, 12, 64, 22, 11, 90]
#   j=3: [64,22] -> zamiana -> [22,64]
#        lista = [34, 25, 12, 22, 64, 11, 90]
#   j=4: [64,11] -> zamiana -> [11,64]
#        lista = [34, 25, 12, 22, 11, 64, 90]
#   j=5: [64,90] -> bez zamiany
#        lista = [34, 25, 12, 22, 11, 64, 90]
#
# Przejście 2:
#   j=0: [34,25] -> zamiana -> [25,34]
#        lista = [25, 34, 12, 22, 11, 64, 90]
#   j=1: [34,12] -> zamiana -> [12,34]
#        lista = [25, 12, 34, 22, 11, 64, 90]
#   j=2: [34,22] -> zamiana -> [22,34]
#        lista = [25, 12, 22, 34, 11, 64, 90]
#   j=3: [34,11] -> zamiana -> [11,34]
#        lista = [25, 12, 22, 11, 34, 64, 90]
#   j=4: [34,64] -> bez zamiany
#        lista = [25, 12, 22, 11, 34, 64, 90]
#
# Przejście 3:
#   j=0: [25,12] -> zamiana -> [12,25]
#        lista = [12, 25, 22, 11, 34, 64, 90]
#   j=1: [25,22] -> zamiana -> [22,25]
#        lista = [12, 22, 25, 11, 34, 64, 90]
#   j=2: [25,11] -> zamiana -> [11,25]
#        lista = [12, 22, 11, 25, 34, 64, 90]
#   j=3: [25,34] -> bez zamiany
#
# Przejście 4:
#   j=0: [12,22] -> bez zamiany
#   j=1: [22,11] -> zamiana -> [11,22]
#        lista = [12, 11, 22, 25, 34, 64, 90]
#   j=2: [22,25] -> bez zamiany
#
# Przejście 5:
#   j=0: [12,11] -> zamiana -> [11,12]
#        lista = [11, 12, 22, 25, 34, 64, 90]
#   j=1: [12,22] -> bez zamiany
#
# Przejście 6:
#   j=0: [11,12] -> bez zamiany
#   Nie było żadnej zamiany, więc kończymy sortowanie
#
# Koniec: lista = [11, 12, 22, 25, 34, 64, 90]

# Czyli:
def bubble_sort(lista):
    n = len(lista)
    for i in range(n - 1):
        zamiana = False
        for j in range(n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                zamiana = True
        if not zamiana:
            break
    return lista

# poćwicz ten algorytm, próbując go napisać samemu niżej :)