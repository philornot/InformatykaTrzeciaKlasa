from interfejs import zamien_na_bin


def zapisz_w_tablicy(n, w=3, k=3):
    n = zamien_na_bin(int(n), zwroc_str=True)
    kratka = {}
    for cyfra in n:
        print(f'\nCyfra {cyfra}')
        for w_i in range(w):
            for k_i in range(k):
                kratka[w_i, k_i] = cyfra
                print(f'({w_i}, {k_i}) = {cyfra}')

liczba = 4
print(f'{liczba} to {zamien_na_bin(liczba)}')
print(zapisz_w_tablicy(4))
