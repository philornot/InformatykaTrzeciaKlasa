def algorytm(lista_liczb_n, b=1, c=0):
    try:
        for n in lista_liczb_n:
            n_origin = n
            a = n % 10
            n = n % 10
            if a % 2 == 0:
                c = c + b * (a % 2)
                print(f'dla {n_origin} c={c}')
            else:
                c = c + b
                print(f'dla {n_origin} c={c}')
            b = b * 10

    except TypeError:
        n = lista_liczb_n
        n_origin = n
        a = n % 10
        n = n % 10
        if a % 2 == 0:
            c = c + b * (a % 2)
            print(f'dla {n_origin} c={c}')
        else:
            c = c + b
            print(f'dla {n_origin} c={c}')
        b = b * 10


# noinspection PyTypeChecker
algorytm(10)
