def algorytm(n):
    b = 1
    c = 0
    licznik_c_plus_b = 0

    while n > 0:
        print(f'a = {n} % 10 ({n % 10})')
        a = n % 10

        print(f'n = {n} // 10 ({n // 10})')
        n = n // 10

        if a % 2 == 0:
            print(f'a jest parzyste (a % 2 = {a%2})')
            print(f'c = {c} + {b} * ({a} // 2) = {c + b * (a // 2)}')
            c = c + b * (a // 2)

        else:
            print(f'c = {c} + {b} ({c + b})')
            c = c + b

            licznik_c_plus_b += 1
            print(f'licznik_c_plus_b={licznik_c_plus_b}')

        print(f'b = {b} * 10 ({b * 10})\n\n===========\n')
        b = b * 10

    return c, licznik_c_plus_b
