from main import dane

l = dane()
l2 = []

for i in range(len(l)):
    l2.append(int(l[i][:-1], int(l[i][-1])))

najw = max(l2)
kod_najw = l[l2.index(najw)]
najm = min(l2)
kod_najm = l[l2.index(najm)]

print(najw, kod_najw)
print(najm, kod_najm)