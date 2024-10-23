from interfejs import licz_bloki

bin_txt = '../../dane2023maj/bin_przyklad.txt'

linijki_clean = []
with open(bin_txt) as plik:
    linijki = plik.readlines()
    for linijka in linijki:
        linijka = linijka.strip()
        linijki_clean.append(linijka)

licznik = 0
for binary in linijki_clean:
    print(binary)
    if licz_bloki(binary) <= 2:
        licznik += 1

print(f'Dla pliku {bin_txt} odpowiedzią jest {licznik}')
