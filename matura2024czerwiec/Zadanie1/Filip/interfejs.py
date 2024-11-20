def zamien_na_bin(liczba, zwroc_str=True):
    if liczba == 0:
        return 0

    liczba_bin = ""

    while liczba > 0:
        liczba_bin = str(liczba % 2) + liczba_bin
        liczba = liczba // 2

    if zwroc_str:
        return liczba_bin
    else:
        return int(liczba_bin)
