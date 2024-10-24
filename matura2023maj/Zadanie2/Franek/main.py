def ile_bloków(n):
    b = 1
    obc = n[0]
    for i in range(1, len(n)):
        if obc != n[i]:
            b += 1
            obc = n[i]
    return b

def lista_danych():
    L = list(open("../../dane2023maj/bin.txt", "r"))
    for i in range(len(L)):
        L[i] = L[i].strip()
    return L