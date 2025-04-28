def czytaj_dane(czy_przyklad=False):
    if czy_przyklad:
        plik = '../../dane2021czerwiec/przyklad.txt'
    else:
        plik = '../../dane2021czerwiec/napisy.txt'

    with open(plik, 'r') as f:
        dane = f.readlines()
    dane_clean = []
    for dana in dane:
        dana = dana.strip()
        dane_clean.append(dana)

    return dane_clean

def zapisz_wynik(odpowiedz):
    with open('wyniki4.txt', 'r') as f:
        aktualny_wynik = f.read()

    with open('wyniki4.txt', 'w') as f:
        f.write(f'{aktualny_wynik}\n'
                f'=====\n'
                f'Zadanie 4.1\n'
                f'{odpowiedz}')