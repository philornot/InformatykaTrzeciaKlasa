from interfejs import licz_bloki, czytaj_plik

linijki_clean = czytaj_plik(czy_przyklad=False)

licznik = 0
for binary in linijki_clean:
    print(binary)
    if licz_bloki(binary) <= 2:
        licznik += 1

print(f'Odpowiedź: {licznik}')
