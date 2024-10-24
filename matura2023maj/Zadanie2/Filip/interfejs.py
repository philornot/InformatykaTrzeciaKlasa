def decimal_to_binary(liczba_10):
    if liczba_10 == 0:
        return "0"

    binary = ""
    num = liczba_10

    while num > 0:
        binary = str(num % 2) + binary
        num = num // 2

    return binary


def binary_to_decimal(binary_str):
    decimal = 0
    power = 0

    for bit in reversed(binary_str):
        if bit == '1':
            decimal += 2 ** power
        power += 1

    return decimal


def licz_bloki(binary):
    ostatni_znak = ''
    licznik_blokow = 0

    for char in binary:
        if char != ostatni_znak:
            licznik_blokow += 1
            ostatni_znak = char

    return licznik_blokow


def czytaj_plik(czy_przyklad=False):
    if czy_przyklad is True:
        file = '../../dane2023maj/bin_przyklad.txt'
    else:
        file = '../../dane2023maj/bin.txt'

    linijki_clean = []
    with open(file) as plik:
        linijki = plik.readlines()
        for linijka in linijki:
            linijka = linijka.strip()
            linijki_clean.append(linijka)

    return linijki_clean
