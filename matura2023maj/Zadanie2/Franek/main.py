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
    return (L)

def XOR(a,b):
    a1 = bin(a)[2::]
    b1 = bin(b)[2::]
    if len(a1) > len(b1):
        for i in range(len(a1)-len(b1)):
            b1 = "".join(("0",b1))
    if len(b1) > len(a1):
        for i in range(len(b1)-len(a1)):
            a1 = "".join(("0",a1))
    wyn = ''
    for i in range(len(a1)):
        if a1[i] == b1[i]:
            wyn += "0"
        else:
            wyn += "1"
    return(int(wyn,2))