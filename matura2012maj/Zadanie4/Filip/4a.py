plik_tekst = open("../../dane2012maj/tj.txt", "r")
tekst_jawny = plik_tekst.read()
plik_tekst.close()

plik_klucz = open("klucze1.txt", "r")
klucz_raw = plik_klucz.read()
plik_klucz.close()

klucz = ""
for znak in klucz_raw:
    if znak >= 'A' and znak <= 'Z':
        klucz = klucz + znak

szyfrogram = ""
pozycja_klucza = 0
for i in range(len(tekst_jawny)):
    litera_tekstu = tekst_jawny[i]

    if litera_tekstu >= 'A' and litera_tekstu <= 'Z':
        litera_klucza = klucz[pozycja_klucza % len(klucz)]

        kod_tekstu = ord(litera_tekstu)
        wartosc_klucza = ord(litera_klucza) - 64

        suma = kod_tekstu + wartosc_klucza
        if suma > 90:
            suma = suma - 26

        szyfrogram = szyfrogram + chr(suma)
        pozycja_klucza = pozycja_klucza + 1
    else:
        szyfrogram = szyfrogram + litera_tekstu

plik_wynik = open("wynik4a.txt", "w")
plik_wynik.write(szyfrogram)
plik_wynik.close()