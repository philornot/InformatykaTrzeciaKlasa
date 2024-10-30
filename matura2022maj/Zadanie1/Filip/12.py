lista = [2, 2, 2, 2, 2]
n = len(lista)
licznik = 0
zmiany = 0

for i in range(n):
    # print(f'Sprawdzam {n - licznik}')

    if n - licznik not in lista:
        # print(f'Ciąg nie zawiera liczby {n - licznik}')
        zmiany += 1

    # else:
    #     print(f'{n-licznik} jest w {lista}')

    licznik += 1

print(f'Wymagane zmiany: {zmiany}')
