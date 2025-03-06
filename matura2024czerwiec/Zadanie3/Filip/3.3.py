from interfejs import czytaj_plik

slowa = czytaj_plik(czy_przyklad=False)

def sprawdz_czy_litera_jest_w_wiekszosci_pozycji(slowo, litera):
    dlugosc_slowa = len(slowo)
    wystapienia = 0

    for l in slowo:
        if l == litera:
            wystapienia += 1

    if wystapienia / dlugosc_slowa >= 0.5:
        return True
    else:
        return False

def glowna_funkcja_dla_ktorej_nie_mam_kreatywnej_nazwy(slowo):
    for litera in slowo:
        if sprawdz_czy_litera_jest_w_wiekszosci_pozycji(slowo, litera):
            return True

    return False

# print(sprawdz_czy_litera_jest_w_wiekszosci_pozycji('owocowo', 'o'))
# print(sprawdz_czy_litera_jest_w_wiekszosci_pozycji('ambaras', 'a'))

for slowo in slowa:
    if glowna_funkcja_dla_ktorej_nie_mam_kreatywnej_nazwy(slowo):
        print(slowo)

