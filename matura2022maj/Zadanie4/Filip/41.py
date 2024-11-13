# noinspection PyUnresolvedReferences
from interfejs import czytaj_plik, przyklad_txt, liczby_txt

# liczby = czytaj_plik(plik=przyklad_txt)
liczby = czytaj_plik(plik=liczby_txt)
licznik = 0
pierwsza = None

for liczba in liczby:
    liczba = str(liczba)
    if liczba[0] == liczba[-1]:
        if licznik == 0:
            pierwsza = liczba
        licznik += 1

print(f'Licznik: {licznik}\nPierwsza liczba: {pierwsza}')
