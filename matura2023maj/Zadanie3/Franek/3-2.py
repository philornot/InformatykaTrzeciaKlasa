def pary():
    opc = []
    lpar = []
    for i in range(10):
        opc.append(str(i))
    for i in range(10):
        for j in range(10):
            lpar.append(opc[i]+opc[j])
    return lpar

print(pary(),len(pary()))