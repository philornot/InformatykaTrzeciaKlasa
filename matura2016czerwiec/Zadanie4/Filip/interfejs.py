def czytaj_tablice_punktow():
    plik = '../../dane2016czerwiec/punkty.txt'
    with open(plik, "r") as f:
        linie = f.readlines()

    linie_clean = []
    for linia in linie:
        linia_clean = linia.strip()
        linie_clean.append(linia_clean)

    lista_z_punktami_w_tuplach = []
    for i in linie_clean:
        x, y = i.split(' ')
        lista_z_punktami_w_tuplach.append((int(x), int(y)))

    return lista_z_punktami_w_tuplach

