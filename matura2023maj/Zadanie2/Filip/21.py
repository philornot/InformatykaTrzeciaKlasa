from interfejs import decimal_to_binary, licz_bloki

n = decimal_to_binary(int(input("Wprowadź dodatnią całkowitą liczbę n: ")))
print(f'W liczbie {n} jest tyle "bloków": {licz_bloki(n)}')
