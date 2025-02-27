from interfejs import czytaj_plik

slowa = czytaj_plik(czy_przyklad=True)

def koduj_litere_rot13(litera_alfabetu):
    alfabet = [chr(i) for i in range(97, 123)]  # to zwraca angielski alfabet :)
    if litera_alfabetu in alfabet:
        indeks = alfabet.index(litera_alfabetu)
        return alfabet[(indeks + 13) % 26]
    else:
        return litera_alfabetu  # zwraca znaki niebędące literami bez zmian

def koduj_slowo_rot13(slowo):
    zakodowane_slowo = ''
    for litera in slowo:
        zakodowane_slowo += koduj_litere_rot13(litera)
    return zakodowane_slowo

def czytaj_slowo_od_tylu(slowo):
    litery = []
    for litera in slowo:
        litery.append(litera)
    return litt.reverse()

print(czytaj_slowo_od_tylu('nera'))