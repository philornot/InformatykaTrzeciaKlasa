def pary():
    opc = []
    lpar = []
    for i in range(10):
        opc.append(str(i))
    for i in range(10):
        for j in range(10):
            lpar.append(opc[i]+opc[j])
    return lpar

from main import tab, dublet

lds = dublet(tab())
lp = pary()
lip = []
for i in range(100):
    lip.append(lds.count(lp[i]))

najw = [lp[lip.index(max(lip))],max(lip)]
print(najw)

najm = ['ph',najw[1]]
for i in range(100):
    if lip[i] > 0 and lip[i] < najm[1]:
        najm[0],najm[1] = lp[lip.index(lip[i])], lip[i]

print(najm)