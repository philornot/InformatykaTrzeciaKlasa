def algorytm(n):
    b = 1
    c = 0
    licznik_c_plus_b = 0
    while n > 0:
        a = n % 10
        n = n // 10
        if a % 2 == 0:
            c = c + b * (a % 2)
        else:
            c = c + b
            licznik_c_plus_b += 1
        b = b * 10
    return c, licznik_c_plus_b
