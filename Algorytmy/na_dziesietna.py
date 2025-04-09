def zamien_na_dziesietna(liczba, system=4):
    dziesietna = 0
    baza = 1
    while (liczba):
        ostatnia_cyfra = liczba % 10
        liczba = liczba // 10
        dziesietna += ostatnia_cyfra * baza
        baza = baza * system
    return dziesietna

print(zamien_na_dziesietna(1015,8))