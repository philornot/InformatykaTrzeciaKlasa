def czytaj_plik():
    plik = "../../dane2017czerwiec/punkty.txt"
    with open(plik, "r") as f:
        dane = f.read().splitlines()

    pary = []
    for dana in dane:
        liczba1, liczba2 = dana.split(' ')
        para = int(liczba1), int(liczba2)
        pary.append(para)

    return pary

