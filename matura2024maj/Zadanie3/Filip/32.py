from interfejs import nieparz_skrot


def sprawdz_liczbe_skrotow(file):
    with open(file, encoding="utf-8") as file:
        dane_linie = file.readlines()
    brak_skrotu = 0
    istnieje_skrot = 0
    for dana in dane_linie:
        dana = dana.strip()
        print(f'Dana: {dana}')
        if nieparz_skrot(dana) is None:
            brak_skrotu += 1
            print(f'Skrót nie istnieje ({brak_skrotu})\n')
        else:
            istnieje_skrot += 1
            print(f'Skrót istnieje ({istnieje_skrot})\n')
    return brak_skrotu, istnieje_skrot


plik = "../../../matura2024maj/dane2024maj/skrot.txt"
brak, istnieje = sprawdz_liczbe_skrotow(plik)
print(f'Dla pliku {plik} jest {istnieje} istniejących skrótów oraz {brak} nieistniejących skrótów.')
