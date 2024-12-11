liczby_txt = '../../dane2022maj/liczby.txt'
przyklad_txt = '../../dane2022maj/przyklad11.txt'


def czytaj_plik(plik=liczby_txt):
    linijki = []
    with open(plik, encoding='utf-8') as p:
        linijki_raw = p.readlines()
    for linijka in linijki_raw:
        linijki.append(int(linijka.strip()))

    return linijki


def rozklad_na_czynniki(n):
    if n < 2:
        return []

    czynniki = []
    dzielnik = 2

    while n > 1:
        while n % dzielnik == 0:
            czynniki.append(dzielnik)
            n //= dzielnik
        dzielnik += 1
        if dzielnik * dzielnik > n:
            if n > 1:
                czynniki.append(n)
            break

    return czynniki
