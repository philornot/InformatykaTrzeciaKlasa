plik_szyfrogram = open("../../dane2012maj/sz.txt", "r")
szyfrogram = plik_szyfrogram.read()
plik_szyfrogram.close()

plik_klucz = open("../../dane2012maj/klucze2.txt", "r")
klucz_surowy = plik_klucz.read()
plik_klucz.close()

klucz = ""
for znak in klucz_surowy:
    if znak >= 'A' and znak <= 'Z':
        klucz = klucz + znak

tekst_jawny = ""
pozycja_klucza = 0
for i in range(len(szyfrogram)):
    litera_szyfru = szyfrogram[i]

    if litera_szyfru >= 'A' and litera_szyfru <= 'Z':
        litera_klucza = klucz[pozycja_klucza % len(klucz)]

        kod_szyfru = ord(litera_szyfru)
        wartosc_klucza = ord(litera_klucza) - 64

        roznica = kod_szyfru - wartosc_klucza
        if roznica < 65:
            roznica = roznica + 26

        tekst_jawny = tekst_jawny + chr(roznica)
        pozycja_klucza = pozycja_klucza + 1
    else:
        tekst_jawny = tekst_jawny + litera_szyfru

plik_wynik = open("wynik4b.txt", "w")
plik_wynik.write(tekst_jawny)
plik_wynik.close()