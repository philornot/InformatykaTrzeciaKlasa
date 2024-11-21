from interfejs import zamien_na_bin


def zapisz_w_tablicy(n, w=3, k=3):
    n = zamien_na_bin(int(n), zwroc_str=True)
    kratka = {} # todo: idziemy kolumnami, więc trzeba zamienić iterację (kolejność)
    for cyfra in n:
        print(f'Cyfra {cyfra}')
        for k_i in range(k):
            print(f'Kolumna {k_i}')
            for w_i in range(w):
                print(f'Wiersz {w_i}')
                kratka[w_i, k_i] = cyfra
                print(f'{w_i} {k_i} ==> {cyfra}')


print(zapisz_w_tablicy(4))
print(zamien_na_bin(4))
