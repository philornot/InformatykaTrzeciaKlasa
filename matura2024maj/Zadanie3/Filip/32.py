from interfejs import nieparz_skrot


# Funkcja sprawdzająca liczbę istniejących i nieistniejących nieparzystych skrótów w danym pliku
def sprawdz_liczbe_skrotow(file):
    # Otwórz plik i wczytaj jego linie
    with open(file, encoding="utf-8") as file:
        dane_linie = file.readlines()  # wczytanie wszystkich linii z pliku

    brak_skrotu = 0  # licznik dla liczb, które nie mają nieparzystego skrótu
    istnieje_skrot = 0  # licznik dla liczb, które mają nieparzysty skrót

    # Przeiteruj przez każdą linię w pliku
    for dana in dane_linie:
        dana = dana.strip()  # usuń białe znaki z początku i końca tekstu
        print(f'Dana: {dana}')  # wypisz aktualną liczbę do sprawdzenia

        # Sprawdź, czy istnieje nieparzysty skrót
        if nieparz_skrot(dana) is None:
            brak_skrotu += 1  # zwiększ licznik brakujących skrótów
            print(f'Skrót nie istnieje ({brak_skrotu})\n')
        else:
            istnieje_skrot += 1  # zwiększ licznik istniejących skrótów
            print(f'Skrót istnieje ({istnieje_skrot})\n')

    return brak_skrotu, istnieje_skrot  # zwróć wyniki liczbowe


# Ścieżka do pliku z danymi
plik = "../../../matura2024maj/dane2024maj/skrot.txt"

# Wywołaj funkcję i wypisz podsumowanie dla pliku
brak, istnieje = sprawdz_liczbe_skrotow(plik)
print(f'Dla pliku {plik} jest {istnieje} istniejących skrótów oraz {brak} nieistniejących skrótów.')
