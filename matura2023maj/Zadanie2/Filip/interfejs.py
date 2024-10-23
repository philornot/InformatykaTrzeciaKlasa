def decimal_to_binary(liczba_10):
    if liczba_10 == 0:
        return "0"

    binary = ""
    num = liczba_10

    while num > 0:
        binary = str(num % 2) + binary
        num = num // 2

    return binary

def licz_bloki(binary):
    ostatni_znak = ''
    licznik_blokow = 0

    for char in binary:
        if char != ostatni_znak:
            licznik_blokow += 1
            ostatni_znak = char

    return licznik_blokow