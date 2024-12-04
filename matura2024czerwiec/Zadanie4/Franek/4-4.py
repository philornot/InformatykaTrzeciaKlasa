from main import lista, przesyl_pakietow
l, wyn,kt = lista(), [], [0, 1, 3, 7]
tp = przesyl_pakietow(l)

for i in kt:
    tm = []
    for j in range(len(tp[i])):
        tm.append(tp[i].count(j))
    wyn.append(max(tm))

print(wyn)