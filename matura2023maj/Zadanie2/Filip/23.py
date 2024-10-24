from interfejs import czytaj_plik, binary_to_decimal, decimal_to_binary

linijki_clean = czytaj_plik(czy_przyklad=False)
print(linijki_clean)

maks = 0
for linijka in linijki_clean:
    liczba = int(binary_to_decimal(linijka))
    if liczba > maks:
        maks = liczba

maks = decimal_to_binary(maks)
print(f'Odpowiedź: {maks}')
