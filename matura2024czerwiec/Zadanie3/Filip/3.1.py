from interfejs import czytaj_plik

slowa = czytaj_plik(czy_przyklad=False)

slowa_sample = ['alamakota', 'brokat', 'krata']
znalezione = []

for slowo in slowa:
    i = 0
    for znak in slowo:
        if znak == 'k':
            if i + 2 < len(slowo) and slowo[i + 2] == 't':
                znalezione.append(slowo)
                print(f'{slowo} - {slowo[i]}{slowo[i + 1]}{slowo[i + 2]}')
        i += 1

print(f'Znaleziono {len(znalezione)} napisów {znalezione}')