from interfejs import czytaj_dane, zapisz_wynik

napisy = czytaj_dane(czy_przyklad=False)

haslo = ''
pozycja = 1

for i in range(19, len(napisy), 20):
    print(f'wiersz: {i + 1}, pozycja: {pozycja}, literka: {napisy[i][pozycja - 1]}, napis: {napisy[i]}')
    haslo = haslo + napisy[i][pozycja - 1]
    pozycja += 1

print('\n' + haslo)
zapisz_wynik(odpowiedz=haslo)
