from main import lista, przesyl_pakietow
l = lista()
tp = przesyl_pakietow(l)
wyn = 0
wynt = 0

for i in range(len(tp)):
    for j in range(len(tp[i])):
        if tp[i][j] == j + 1 and wyn == 0:
            wyn = j + 1
            wynt = i + 1

    if wyn != 0:
        break

print(wynt, wyn)