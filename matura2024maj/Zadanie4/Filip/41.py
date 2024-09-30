from interfejs import line_to_list

pierwsza_linia = line_to_list(1)
druga_linia = line_to_list(2)
licznik_dzielnikow = 0
print(f'Pierwsza linia: {pierwsza_linia}')
print(f'Druga linia: {druga_linia}')

for liczba_1 in pierwsza_linia:
    for liczba_2 in druga_linia:
        print(f'Sprawdzam dzielenie {liczba_2}/{liczba_1}')
        if liczba_2 % liczba_1 == 0:
            licznik_dzielnikow += 1
            print(f'Licznik: {licznik_dzielnikow}')

print(licznik_dzielnikow)
