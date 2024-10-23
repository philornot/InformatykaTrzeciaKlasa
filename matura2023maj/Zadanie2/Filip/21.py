from interfejs import decimal_to_binary

n = decimal_to_binary(int(input("Wprowadź dodatnią całkowitą liczbę n: ")))


def licz_bloki(binary):
    ostatni_znak = ''
    licznik_blokow = 0

    for char in binary:
        if char != ostatni_znak:
            licznik_blokow += 1
            ostatni_znak = char

    return licznik_blokow


print(licz_bloki(n))
